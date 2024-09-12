import os
import openai
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set your OpenAI API key and Telegram Token
openai.api_key = "your-openai-api-key"
TELEGRAM_TOKEN = "your-telegram-bot-token"

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(
        f'Hello {user.first_name}, I am a GPT-4o powered bot! Type anything and I will respond.'
    )

# Message handler to respond using GPT-4o
def reply_with_gpt4(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    response = openai.Completion.create(
        engine="gpt-4o",
        prompt=user_message,
        max_tokens=150
    )
    update.message.reply_text(response.choices[0].text.strip())

# Main function to start the bot
def main() -> None:
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_with_gpt4))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
