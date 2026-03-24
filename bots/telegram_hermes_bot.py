import logging
import requests
from telegram import Update, Bot
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext 

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram Bot Token
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Hermes-3 API URL and headers
HERMES_API_URL = 'https://api.hermes3.com/function-calling'
HEADERS = {'Authorization': 'Bearer YOUR_HERMES_API_KEY'}

# Fallback options
ANOTHER_AI_API_URL = 'https://api.anthropic.com/v1/chat'

# Define Bot
bot = Bot(token=TELEGRAM_TOKEN)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your Hermes Telegram Bot integration.')

def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    logger.info(f'Received message: {user_message}')
    try:
        # Call Hermes API
        response = requests.post(HERMES_API_URL, headers=HEADERS, json={'input': user_message})
        response.raise_for_status()
        hermes_response = response.json()
        update.message.reply_text(hermes_response['output'])
    except requests.exceptions.HTTPError as http_err:
        logger.error(f'HTTP error occurred: {http_err}')
        update.message.reply_text('Sorry, there was an error with the Hermes API. Trying fallback.')
        fallback_to_anthropic(user_message, update)
    except Exception as err:
        logger.error(f'Other error occurred: {err}')
        update.message.reply_text('An unexpected error occurred.')

def fallback_to_anthropic(user_message, update):
    response = requests.post(ANOTHER_AI_API_URL, json={'prompt': user_message})
    if response.ok:
        ai_response = response.json()
        update.message.reply_text(ai_response['completion'])
    else:
        update.message.reply_text('Sorry, the fallback service is also unavailable.')

def main() -> None:
    from telegram.ext import Updater
    updater = Updater(token=TELEGRAM_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    logger.info('Bot started!')
    updater.idle()

if __name__ == '__main__':
    main()