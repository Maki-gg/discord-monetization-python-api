"""
MIT License

Copyright (c) 2024-PRESENT Maki (https://maki.gg)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import annotations

from http import HTTPStatus
from typing import (
    Any,
    Callable,
    Coroutine,
    Dict,
    Final,
    Optional,
    Tuple,
    cast,
)

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response
from nacl.signing import VerifyKey

from discord_webhooks.enums import WebhookEventTypeEnum, WebhookTypeEnum

from .types import (
    JSONResponseError,
    WebhookHandler,
    WebhookPayload,
)


__all__: Final[Tuple[str, ...]] = (
    "WebhookService",
)


DEFAULT_FASTAPI_KWARGS: Final[dict[str, Any]] = {
    "debug": False,
    "title": "Discord Webhook",
    "openapi_url": None,
    "docs_url": None,
    "redoc_url": None,
    "swagger_ui_init_oauth": None,
    "include_in_schema": False,
}

ERROR_BAD_SIGNATURE_REQUEST: Final[JSONResponse] = JSONResponse(
    status_code=HTTPStatus.UNAUTHORIZED,
    content=JSONResponseError(
        error="Bad request signature",
    ),
)


class WebhookService:
    __slots__: Final[tuple[str, ...]] = (
        "http",
        "_token",
        "_id",
        "_public_key",
        "_register_commands_on_startup",
        "_fastapi",
        "_event_handlers",
        "_uri_path",
        "_on_startup",
        "_on_shutdown",
    )

    def __init__(
        self,
        *,
        client_public_key: str,
        uri_path: str = "/api/interactions/webhook",
        on_startup: Optional[Callable[[], Coroutine[Any, Any, None]]] = None,
        on_shutdown: Optional[Callable[[], Coroutine[Any, Any, None]]] = None,
        fastapi: Optional[FastAPI] = None,
        **kwargs: Any,
    ) -> None:
        """ Create an HTTPBot client. """
        if (
            fastapi is not None
            and (
                on_startup is not None
                or on_shutdown is not None
            )
        ):
            raise RuntimeError("`fastapi` kwarg cannot be provided as well as `on_startup` or `on_shutdown` kwarg.")

        self._on_startup: Optional[Callable[[], Coroutine[Any, Any, None]]] = on_startup
        self._on_shutdown: Optional[Callable[[], Coroutine[Any, Any, None]]] = on_shutdown
        self._public_key: Final[str] = client_public_key
        self._fastapi = fastapi or FastAPI(
            **DEFAULT_FASTAPI_KWARGS,
            **kwargs,
            on_startup=[self._setup],
            on_shutdown=[self._shutdown],
        )
        self._event_handlers: Dict[WebhookEventTypeEnum, WebhookHandler] = {}
        self._uri_path: str = uri_path
        self._fastapi.add_api_route(
            path=self._uri_path,
            endpoint=self._webook_callback,
            name="Discord Webhook entry point",
            methods=["POST"],
        )

    def command(self, event: WebhookEventTypeEnum) -> Callable[[WebhookHandler], None]:
        def _decorator(func: WebhookHandler) -> None:
            self._event_handlers[event] = func
        return _decorator

    async def _verify_signature(self, request: Request) -> bool:
        signature: str | None = request.headers.get('X-Signature-Ed25519')
        timestamp: str | None = request.headers.get('X-Signature-Timestamp')
        if (
            signature is None
            or timestamp is None
        ):
            return False
        else:
            message = timestamp.encode() + await request.body()
            try:
                vk = VerifyKey(bytes.fromhex(self._public_key))
                vk.verify(message, bytes.fromhex(signature))
            except Exception:
                return False
        return True

    async def _handle_verified_webhook(self, request: Request) -> Response:
        request_json = cast(WebhookPayload, await request.json())
        if request_json["type"] == WebhookTypeEnum.PING:
            return Response(
                status_code=HTTPStatus.NO_CONTENT,
            )

        event_type = WebhookEventTypeEnum(request_json["event"]["type"])
        event_handler_function = self._event_handlers.get(event_type, None)
        if event_handler_function is not None:
            await event_handler_function(request_json["event"])  # pyright: ignore[reportArgumentType] - open to suggestions on how to get around this pyright ignore
        return Response(status_code=HTTPStatus.NO_CONTENT)

    async def _webook_callback(self, request: Request) -> Response:
        verified_signature = await self._verify_signature(request)
        if not verified_signature:
            return ERROR_BAD_SIGNATURE_REQUEST

        return await self._handle_verified_webhook(request)

    async def _setup(self) -> None:
        if self._on_startup is not None:
            await self._on_startup()

    async def _shutdown(self) -> None:
        if self._on_shutdown is not None:
            await self._on_shutdown()

    def start(self, **kwargs: Any) -> None:
        uvicorn.run(app=self._fastapi, **kwargs)
