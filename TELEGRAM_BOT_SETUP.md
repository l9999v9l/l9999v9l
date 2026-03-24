# Quick-Start Deployment Guide for Telegram Bot

## Step 1: Generate Your Bot Token
1. Open the Telegram app.
2. Search for the user `@BotFather` and start a chat.
3. Send the command `/newbot`.
4. Follow the instructions to set your bot's name and username.
5. After completing the setup, you will receive a token for your bot. Save this token as you will need it for the next steps.

## Step 2: Configure the API Key
1. In your project directory, create a `.env` file (if not already created).
2. Add the following line to the `.env` file:
   
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```
   Replace `your_bot_token_here` with the token you received from `@BotFather`.

## Step 3: One-Command Deployment
1. In the terminal, navigate to your project directory.
2. Run the following command to deploy your Telegram bot:
   
   ```bash
   npm run deploy
   ```

   This command will build and deploy your bot instantly.

## Additional Information
- Make sure you have all necessary dependencies installed.
- Refer to the [Telegram Bot API Documentation](https://core.telegram.org/bots/api) for more details on bot functionalities.