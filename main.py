from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import register_handlers
import asyncio


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    register_handlers(dp)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
