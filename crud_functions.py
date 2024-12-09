import sqlite3

connection = sqlite3.connect('not_telegram2.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    ''')
    connection.commit()

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()

def add_product(title, description, price):
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', (title, description, price))
    connection.commit()

def populate_products():
    products = [
        ('Product1', 'Описание 1', 100),
        ('Product2', 'Описание 2', 200),
        ('Product3', 'Описание 3', 300),
        ('Product4', 'Описание 4', 400)
    ]
    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)
    connection.commit()

def close_connection():
    connection.close()