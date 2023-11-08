import sqlite3

def create():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER,
    quantity INTEGER
    )""")

    conn.commit()
    conn.close()

create()

def add():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    name = input("name: ")
    price = input("price: ")
    quantity = input("quantity: ")

    cursor.execute('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)',
                       (name, price, quantity))
    conn.commit()
    conn.close()
add()


def get():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM products""")

    result = cursor.fetchall()
    print(result)
    conn.close()

get()

