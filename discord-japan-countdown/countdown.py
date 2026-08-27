import json
import os
import sys
import urllib.request
from datetime import date, datetime
from zoneinfo import ZoneInfo

TIMEZONE = ZoneInfo("Europe/Jersey")
TARGET_DATE = date(2026, 11, 20)
MESSAGE_TEMPLATE = "{days} days until Japan Trip!"


def main():
    now = datetime.now(TIMEZONE)

    # GitHub Actions runs at both 23:00 UTC and 00:00 UTC so this works
    # correctly during both BST and GMT. Only the run that lands in the
    # local midnight hour is allowed to post.
    if now.hour != 0:
        print(f"Skipping: local time is {now:%Y-%m-%d %H:%M %Z}, not midnight.")
        return

    today = now.date()
    days = (TARGET_DATE - today).days

    # Stop posting after the target date.
    if days < 0:
        print("Countdown is complete. Nothing to post.")
        return

    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("Missing DISCORD_WEBHOOK_URL secret.", file=sys.stderr)
        sys.exit(1)

    message = MESSAGE_TEMPLATE.format(days=days)
    payload = json.dumps({"content": message}).encode("utf-8")

    request = urllib.request.Request(
        webhook_url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "DiscordJapanCountdown/1.0",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            if response.status not in (200, 204):
                raise RuntimeError(f"Discord returned HTTP {response.status}")
    except Exception as exc:
        print(f"Failed to post to Discord: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Posted: {message}")


if __name__ == "__main__":
    main()
