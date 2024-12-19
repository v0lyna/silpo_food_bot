from datetime import datetime
from telebot import TeleBot
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


def register_handlers(bot: TeleBot):
    db = Database(DB_FILE)

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(
            message.chat.id,
            WELCOME_MESSAGE,
            reply_markup=create_main_menu_keyboard()
        )

    @bot.message_handler(commands=['help'])
    def help(message):
        bot.send_message(message.chat.id, HELP_MESSAGE)

    @bot.message_handler(commands=['site'])
    def site(message):
        keyboard = create_inline_website_keyboard()
        bot.send_message(
            message.chat.id,
            "Натисніть кнопку для переходу на сайт Сільпо:",
            reply_markup=keyboard
        )

    @bot.message_handler(commands=['inform'])
    def inform(message):
        keyboard = create_inline_welcome_keyboard()
        bot.send_message(
            message.chat.id,
            "Натисніть кнопку для отримання інформації про Сільпо:",
            reply_markup=keyboard
        )

    @bot.callback_query_handler(func=lambda call: True)
    def callback_handler(call):
        if call.data == "welcome":
            try:
                with open(WELCOME_IMAGE_PATH, 'rb') as photo:
                    bot.send_photo(
                        call.message.chat.id,
                        photo,
                        caption=STORE_INFO
                    )
            except Exception as e:
                bot.send_message(
                    call.message.chat.id,
                    "Вибачте, виникла помилка при завантаженні зображення."
                )

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        if message.text == 'Продукти':
            bot.send_message(
                message.chat.id,
                "Виберіть категорію продуктів:",
                reply_markup=create_products_menu_keyboard()
            )
        elif message.text == 'Назад до меню':
            bot.send_message(
                message.chat.id,
                "Головне меню:",
                reply_markup=create_main_menu_keyboard()
            )
        elif message.text == 'Назад до категорій':
            bot.send_message(
                message.chat.id,
                "Виберіть категорію продуктів:",
                reply_markup=create_products_menu_keyboard()
            )
        elif message.text in ['М\'ясо', 'Риба', 'Овочі', 'Фрукти', 'Бакалія']:
            bot.send_message(
                message.chat.id,
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

                        bot.send_message(
                            message.chat.id,
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
                bot.send_message(message.chat.id, orders_text)
            else:
                bot.send_message(
                    message.chat.id,
                    "У вас поки немає замовлень"
                )

        elif message.text == 'Очистити замовлення':
            deleted_count = db.clear_user_orders(message.from_user.id)
            if deleted_count > 0:
                bot.send_message(
                    message.chat.id,
                    f"Видалено {deleted_count} замовлень"
                )
            else:
                bot.send_message(
                    message.chat.id,
                    "У вас немає замовлень для видалення"
                )
