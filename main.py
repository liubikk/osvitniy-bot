import telebot

TOKEN = "8472813077:AAE7dOUOjDcGPnJf0_C2tmdKniFE9Hk1zl4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    name = message.from_user.first_name
    bot.reply_to(message, f"Привіт, {name}! 👋\n\nЦе освітній бот НПУ.\nЩо вміє цей бот?\n- Відповідає на питання студентів\n- Дає корисну інформацію\n- Дозволяє звернутись до техпідтримки 🧑‍💻")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Тут можна зробити систему з техпідтримкою
    bot.reply_to(message, "Ваше повідомлення передано техпідтримці ❤️")

bot.polling()
