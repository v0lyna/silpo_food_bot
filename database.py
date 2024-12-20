import aiosqlite
from datetime import datetime
from typing import List, Tuple


class Database:
    def __init__(self, db_file: str):
        self.db_file = db_file

    async def init_db(self):
        """Ініціалізація бази даних та створення таблиці orders"""
        async with aiosqlite.connect(self.db_file) as db:
            await db.execute('''
                CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    username TEXT,
                    product TEXT NOT NULL,
                    price REAL NOT NULL,
                    order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            await db.commit()

    async def add_order(self, user_id: int, username: str, product: str, price: float) -> None:
        """Додавання нового замовлення"""
        async with aiosqlite.connect(self.db_file) as db:
            await db.execute('''
                INSERT INTO orders (user_id, username, product, price, order_time)
                VALUES (?, ?, ?, ?, ?)
            ''', (user_id, username, product, price, datetime.now()))
            await db.commit()

    async def get_user_orders(self, user_id: int) -> List[Tuple[str, float, str]]:
        """Отримання всіх замовлень користувача"""
        async with aiosqlite.connect(self.db_file) as db:
            async with db.execute('''
                SELECT product, price, order_time
                FROM orders
                WHERE user_id = ?
                ORDER BY order_time DESC
            ''', (user_id,)) as cursor:
                return await cursor.fetchall()

    async def clear_user_orders(self, user_id: int) -> int:
        """Видалення всіх замовлень користувача"""
        async with aiosqlite.connect(self.db_file) as db:
            cursor = await db.execute(
                'DELETE FROM orders WHERE user_id = ?',
                (user_id,)
            )
            deleted_count = cursor.rowcount
            await db.commit()
            return deleted_count
