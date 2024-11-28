import uvicorn
from fastapi import FastAPI

from discord_webhooks import (
    WebhookEventTypeEnum,
    WebhookPayloadEventApplicationAuthorized,
    WebhookPayloadEventEntitlementCreate,
    WebhookPayloadEventQuestUserEnrollment,
    WebhookService,
)


fastapi = FastAPI()


wh = WebhookService(
    client_public_key="YOUR_CLIENT_PUBLIC_KEY_GOES_HERE",
    fastapi=fastapi,
)


@wh.command(event=WebhookEventTypeEnum.APPLICATION_AUTHORIZED)
async def application_added_to_new_guild(event: WebhookPayloadEventApplicationAuthorized) -> None:
    print(f"App added to {event['data']['guild']['id']} by @{event['data']['user']['username']}!")


@wh.command(event=WebhookEventTypeEnum.ENTITLEMENT_CREATE)
async def new_entitlement_created(event: WebhookPayloadEventEntitlementCreate) -> None:
    print(f"New entitlement with ID {event['data']['id']}!")


@wh.command(event=WebhookEventTypeEnum.QUEST_USER_ENROLLMENT)
async def new_quest_user_enrollment(event: WebhookPayloadEventQuestUserEnrollment) -> None:
    print(f"This is undocumented, your guess is as good as ours.")


if __name__ == "__main__":
    uvicorn.run(app=fastapi)
