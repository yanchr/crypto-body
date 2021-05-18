import telegramConstants as keys
from telegram.ext import *
import telegramResponse as R

def start_command(update, context):
    update.message.reply_text('Hey User, how can I help you?')

def help_command(update, context):
    update.message.reply_text("" + 
    "You can use this comands = " + 
    "/showcoins")
        
    

def handle_message(update, context):
    text = str(update.message.text).lower()
    print(text)
    response = R.simple_responses(text)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dispatcher = updater.dispatcher
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

print("Bot started...")
main()