from telebot import TeleBot
from config import WELCOME_MESSAGE, HELP_MESSAGE, STORE_INFO, WELCOME_IMAGE_PATH, WEB_SITE
from keyboards import (
    create_inline_welcome_keyboard,
    create_main_menu_keyboard,
    create_secondary_menu_keyboard,
    create_products_menu_keyboard,
    create_category_products_keyboard,
    create_inline_website_keyboard,
)


def register_handlers(bot: TeleBot):
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
        elif message.text == 'Акції':
            bot.send_message(
                message.chat.id,
                "Актуальні акції та знижки:",
                reply_markup=create_secondary_menu_keyboard()
            )
        elif message.text == 'Кошик':
            # TODO: Реалізувати функціонал кошика
            bot.send_message(
                message.chat.id,
                "Ваш кошик поки що порожній"
            )
