import telebot
from Text_Check import translate


TOKEN = "Paste your API key here"

bot = telebot.TeleBot(TOKEN)


# Handle the /start and /help commands
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
  bot.reply_to(
      message, "Hello! I am your personal Translator which can translate for you. \nHow can I help you today?"
  )


# Handle all other text messages with a simple echo
@bot.message_handler(func=lambda message: True)
def echo_all(message):
  reply = translate(message.text)
  bot.reply_to(message, f"Here is the translated version of your text:\n{reply}")


# Start the bot
print("Bot is running...")
bot.infinity_polling()


