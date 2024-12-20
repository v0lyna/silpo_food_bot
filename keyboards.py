from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)
from config import WEB_SITE
from products import get_products_keyboard


def create_inline_website_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Відкрити сайт Сільпо", url=WEB_SITE)]
    ])
    return keyboard


def create_inline_welcome_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Привітання", callback_data="welcome")]
    ])
    return keyboard


def create_main_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Продукти'),
                KeyboardButton(text='Напої'),
                KeyboardButton(text='Солодощі')
            ],
            [
                KeyboardButton(text='Мої замовлення'),
                KeyboardButton(text='Очистити замовлення')
            ]
        ],
        resize_keyboard=True,
        row_width=3
    )
    return keyboard


def create_products_menu_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='М\'ясо'),
                KeyboardButton(text='Риба')
            ],
            [
                KeyboardButton(text='Овочі'),
                KeyboardButton(text='Фрукти'),
                KeyboardButton(text='Бакалія')
            ],
            [KeyboardButton(text='Назад до меню')]
        ],
        resize_keyboard=True,
        row_width=3
    )
    return keyboard


def create_category_products_keyboard(category: str) -> ReplyKeyboardMarkup:
    products = get_products_keyboard(category)

    product_buttons = [
        [KeyboardButton(text=f"Замовити {product}")]
        for product in products
    ]

    # Додаємо навігаційні кнопки
    navigation_buttons = [
        [KeyboardButton(text='Назад до категорій')],
        [
            KeyboardButton(text='Мої замовлення'),
            KeyboardButton(text='Очистити замовлення')
        ]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=product_buttons + navigation_buttons,
        resize_keyboard=True,
        row_width=2
    )

    return keyboard
