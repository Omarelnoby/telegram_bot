import telebot

# Replace with your bot's token from BotFather
BOT_TOKEN = '7004455877:AAE30ObcdzyapkJ_vdzuBfE0UOsbwdv_TlM'

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Mapping of user inputs to Google Drive URLs
google_drive_links = {
    "report": "https://drive.google.com/file/d/xxxxxx",
    "sales": "https://drive.google.com/file/d/yyyyyy",
    "data": "https://drive.google.com/file/d/zzzzzz"
}

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_message = (
        "Hi! Send me a keyword like 'report', 'sales', or 'data', "
        "and I'll provide the corresponding Google Drive link."
    )
    bot.reply_to(message, welcome_message)

# Message handler for user input
@bot.message_handler(func=lambda message: True)  # Handle all text messages
def handle_message(message):
    user_input = message.text.lower()  # Convert input to lowercase for case-insensitive matching
    response = google_drive_links.get(user_input, "Sorry, I don't have a link for that keyword.")
    bot.reply_to(message, response)

# Polling to keep the bot running
bot.polling()
