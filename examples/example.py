from discord_webhooks import (
    WebhookEventTypeEnum,
    WebhookPayloadEventApplicationAuthorized,
    WebhookPayloadEventEntitlementCreate,
    WebhookPayloadEventQuestUserEnrollment,
    WebhookService,
)


async def on_startup() -> None:
    print("Webhook listener active!")


wh = WebhookService(
    client_public_key="YOUR_CLIENT_PUBLIC_KEY_GOES_HERE",
    on_startup=on_startup,  # Optional kwarg.
    # on_shutdown also exists!
    uri_path="/api/interactions/webhook",  # You can change the entry point.
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
    wh.start()
