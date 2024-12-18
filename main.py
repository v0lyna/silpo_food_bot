from telebot import TeleBot
from config import BOT_TOKEN
from handlers import register_handlers


def main():
    bot = TeleBot(BOT_TOKEN)
    
    register_handlers(bot)
    
    print("Бот запущений...")
    bot.infinity_polling()


if __name__ == "__main__":
    main()
