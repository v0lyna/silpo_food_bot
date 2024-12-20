from datetime import datetime
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.filters import Command
from config import DB_FILE, WELCOME_MESSAGE, HELP_MESSAGE, STORE_INFO, WELCOME_IMAGE_PATH
from keyboards import (
    create_inline_welcome_keyboard,
    create_main_menu_keyboard,
    create_products_menu_keyboard,
    create_category_products_keyboard,
    create_inline_website_keyboard,
)
from database import Database
from products import PRODUCTS

router = Router()
db = Database(DB_FILE)
db.init_db()


@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        WELCOME_MESSAGE,
        reply_markup=create_main_menu_keyboard()
    )


@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(HELP_MESSAGE)


@router.message(Command("site"))
async def site_command(message: Message):
    keyboard = create_inline_website_keyboard()
    await message.answer(
        "Натисніть кнопку для переходу на сайт Сільпо:",
        reply_markup=keyboard
    )


@router.message(Command("inform"))
async def inform_command(message: Message):
    keyboard = create_inline_welcome_keyboard()
    await message.answer(
        "Натисніть кнопку для отримання інформації про Сільпо:",
        reply_markup=keyboard
    )


@router.callback_query()
async def callback_handler(call: CallbackQuery):
    if call.data == "welcome":
        try:
            photo = InputFile(WELCOME_IMAGE_PATH)
            await call.message.answer_photo(
                photo,
                caption=STORE_INFO
            )
        except Exception as e:
            await call.message.answer(
                f"Вибачте, виникла помилка при завантаженні зображення."
            )
    await call.answer()


@router.message(F.text)
async def handle_text(message: Message):
    if message.text == 'Продукти':
        await message.answer(
            "Виберіть категорію продуктів:",
            reply_markup=create_products_menu_keyboard()
        )

    elif message.text == 'Назад до меню':
        await message.answer(
            "Головне меню:",
            reply_markup=create_main_menu_keyboard()
        )

    elif message.text == 'Назад до категорій':
        await message.answer(
            "Виберіть категорію продуктів:",
            reply_markup=create_products_menu_keyboard()
        )

    elif message.text in ['М\'ясо', 'Риба', 'Овочі', 'Фрукти', 'Бакалія']:
        await message.answer(
            f"Виберіть {message.text.lower()}:",
            reply_markup=create_category_products_keyboard(message.text)
        )

    elif message.text.startswith('Замовити '):
        product_info = message.text.replace('Замовити ', '')
        product_name = product_info.split(' - ')[0]

        for category in PRODUCTS:
            for product in PRODUCTS[category]:
                if product['name'] == product_name:
                    db.add_order(
                        message.from_user.id,
                        message.from_user.username,
                        product_name,
                        product['price']
                    )

                    await message.answer(
                        f"Товар '{product_name}' додано до замовлень!"
                    )
                    return

    elif message.text == 'Мої замовлення':
        orders = db.get_user_orders(message.from_user.id)
        if orders:
            orders_text = "Ваші замовлення:\n\n"
            total_price = 0
            for product, price, order_time in orders:
                order_time = datetime.strptime(order_time, "%Y-%m-%d %H:%M:%S.%f")
                orders_text += f"• {product} - {price}₴ ({order_time:%Y-%m-%d %H:%M})\n"
                total_price += price
            orders_text += f"\nЗагальна сума: {total_price:.1f}₴"
            await message.answer(orders_text)
        else:
            await message.answer("У вас поки немає замовлень")

    elif message.text == 'Очистити замовлення':
        deleted_count = db.clear_user_orders(message.from_user.id)
        if deleted_count > 0:
            await message.answer(f"Видалено {deleted_count} замовлень")
        else:
            await message.answer("У вас немає замовлень для видалення")


def register_handlers(dp):
    dp.include_router(router)
