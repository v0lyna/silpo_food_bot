PRODUCTS = {
    "М'ясо": [
        {"name": "Свинина вирізка", "price": 189.90, "unit": "кг"},
        {"name": "Куряче філе", "price": 159.90, "unit": "кг"},
        {"name": "Яловичина стейк", "price": 299.90, "unit": "кг"},
        {"name": "Індичка філе", "price": 199.90, "unit": "кг"},
        {"name": "Телятина вирізка", "price": 289.90, "unit": "кг"}
    ],
    "Риба": [
        {"name": "Лосось філе", "price": 599.90, "unit": "кг"},
        {"name": "Форель", "price": 499.90, "unit": "кг"},
        {"name": "Тунець стейк", "price": 399.90, "unit": "кг"},
        {"name": "Скумбрія", "price": 199.90, "unit": "кг"},
        {"name": "Дорадо", "price": 399.90, "unit": "кг"}
    ],
    "Овочі": [
        {"name": "Помідори", "price": 69.90, "unit": "кг"},
        {"name": "Огірки", "price": 59.90, "unit": "кг"},
        {"name": "Картопля", "price": 19.90, "unit": "кг"},
        {"name": "Морква", "price": 24.90, "unit": "кг"},
        {"name": "Цибуля", "price": 29.90, "unit": "кг"}
    ],
    "Фрукти": [
        {"name": "Яблука", "price": 39.90, "unit": "кг"},
        {"name": "Банани", "price": 49.90, "unit": "кг"},
        {"name": "Апельсини", "price": 59.90, "unit": "кг"},
        {"name": "Груші", "price": 69.90, "unit": "кг"},
        {"name": "Виноград", "price": 89.90, "unit": "кг"}
    ],
    "Бакалія": [
        {"name": "Рис", "price": 49.90, "unit": "кг"},
        {"name": "Гречка", "price": 69.90, "unit": "кг"},
        {"name": "Макарони", "price": 39.90, "unit": "кг"},
        {"name": "Борошно", "price": 29.90, "unit": "кг"},
        {"name": "Цукор", "price": 34.90, "unit": "кг"}
    ],
    "Напої": [
        {"name": "Кока-кола 2л", "price": 39.90, "unit": "шт"},
        {"name": "Мінеральна вода 1.5л", "price": 19.90, "unit": "шт"},
        {"name": "Сік апельсиновий 1л", "price": 49.90, "unit": "шт"},
        {"name": "Чай чорний 100г", "price": 89.90, "unit": "шт"},
        {"name": "Кава мелена 250г", "price": 199.90, "unit": "шт"}
    ],
    "Солодощі": [
        {"name": "Шоколад молочний", "price": 49.90, "unit": "шт"},
        {"name": "Печиво", "price": 39.90, "unit": "шт"},
        {"name": "Цукерки", "price": 199.90, "unit": "кг"},
        {"name": "Морозиво", "price": 79.90, "unit": "шт"},
        {"name": "Зефір", "price": 89.90, "unit": "шт"}
    ]
}


def get_products_keyboard(category):
    """Returns a list of products of a certain category in a keyboard format"""
    return [f"{product['name']} - {product['price']}₴/{product['unit']}" 
            for product in PRODUCTS.get(category, [])]
