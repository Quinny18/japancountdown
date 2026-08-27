# Discord Japan Trip Countdown

Posts this message to Discord every day at midnight in the Europe/Jersey timezone:

`{days} days until Japan Trip!`

Target date: **20 November 2026**

The countdown posts `0 days until Japan Trip!` on 20 November 2026 and then stops posting.

## Setup

1. Create a new GitHub repository.
2. Upload the contents of this folder, including the hidden `.github` folder.
3. In Discord, open the channel where you want the countdown.
4. Go to **Edit Channel → Integrations → Webhooks → New Webhook**.
5. Copy the webhook URL.
6. In your GitHub repository, go to:
   **Settings → Secrets and variables → Actions → New repository secret**
7. Name the secret exactly:
   `DISCORD_WEBHOOK_URL`
8. Paste the Discord webhook URL as the secret value.
9. Open the repository's **Actions** tab and enable workflows if GitHub asks.
10. To test it, open **Actions → Japan Trip Countdown → Run workflow**.

## Timing note

GitHub Actions scheduled jobs are usually close to the requested time, but GitHub does not guarantee execution at the exact second. The workflow is designed to post during the local midnight hour while correctly handling both GMT and BST.

## Security

Never commit your Discord webhook URL into the repository. Keep it only in the GitHub Actions secret named `DISCORD_WEBHOOK_URL`.
