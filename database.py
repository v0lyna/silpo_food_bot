import sqlite3
from datetime import datetime


class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.init_db()

    def init_db(self):
        """Ініціалізація бази даних та створення таблиці orders"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                username TEXT,
                product TEXT NOT NULL,
                price REAL NOT NULL,
                order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()

    def add_order(self, user_id: int, username: str, product: str, price: float):
        """Додавання нового замовлення"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO orders (user_id, username, product, price, order_time)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, username, product, price, datetime.now()))
        
        conn.commit()
        conn.close()

    def get_user_orders(self, user_id: int):
        """Отримання всіх замовлень користувача"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT product, price, order_time
            FROM orders
            WHERE user_id = ?
            ORDER BY order_time DESC
        ''', (user_id,))
        
        orders = cursor.fetchall()
        conn.close()
        
        return orders

    def clear_user_orders(self, user_id: int):
        """Видалення всіх замовлень користувача"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM orders WHERE user_id = ?', (user_id,))
        
        deleted_count = cursor.rowcount
        conn.commit()
        conn.close()
        
        return deleted_count
