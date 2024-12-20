from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from config import WEB_SITE
from products import get_products_keyboard


def create_inline_website_keyboard():
    keyboard = InlineKeyboardMarkup()
    welcome_button = InlineKeyboardButton(text="Відкрити сайт Сільпо", url=WEB_SITE)
    keyboard.add(welcome_button)
    return keyboard


def create_inline_welcome_keyboard():
    keyboard = InlineKeyboardMarkup()
    welcome_button = InlineKeyboardButton(text="Привітання", callback_data="welcome")
    keyboard.add(welcome_button)
    return keyboard


def create_main_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = KeyboardButton('Продукти')
    btn2 = KeyboardButton('Напої')
    btn3 = KeyboardButton('Солодощі')
    keyboard.add(btn1, btn2, btn3)
    keyboard.add(KeyboardButton('Мої замовлення'), KeyboardButton('Очистити замовлення'))
    return keyboard


def create_products_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = KeyboardButton('М\'ясо')
    btn2 = KeyboardButton('Риба')
    btn3 = KeyboardButton('Овочі')
    btn4 = KeyboardButton('Фрукти')
    btn5 = KeyboardButton('Бакалія')
    btn_back = KeyboardButton('Назад до меню')
    keyboard.add(btn1, btn2)
    keyboard.add(btn3, btn4, btn5)
    keyboard.add(btn_back)
    return keyboard


def create_category_products_keyboard(category):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    products = get_products_keyboard(category)
    buttons = []
    for product in products:
        buttons.append(KeyboardButton(f"Замовити {product}"))

    for i in range(0, len(buttons)):
        keyboard.add(buttons[i])

    keyboard.add(KeyboardButton('Назад до категорій'))
    keyboard.add(KeyboardButton('Мої замовлення'), KeyboardButton('Очистити замовлення'))
    return keyboard
