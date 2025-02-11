import sqlite3

con = sqlite3.connect("laba2.db")

cursor = con.cursor()

cursor.execute("""CREATE TABLE product
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                name TEXT NOT NULL,
                current_price REAL NOT NULL,
                date TEXT NOT NULL)
                """)


cursor.execute("INSERT INTO product (name, current_price, date) VALUES ('Ноутбук', 50000, '2025-01-30')")
cursor.execute("INSERT INTO product (name, current_price, date) VALUES ('Телефон', 70000, '2025-01-30')")
cursor.execute("INSERT INTO product (name, current_price, date) VALUES ('Смартфон', 100000, '2025-01-30')")
cursor.execute("INSERT INTO product (name, current_price, date) VALUES ('ПК', 250000, '2025-01-30')")
cursor.execute("INSERT INTO product (name, current_price, date) VALUES ('Монитор', 525000, '2025-01-30')")
cursor.execute("INSERT INTO product (name, current_price, date) VALUES ('Мышь', 5000, '2025-01-30')")
cursor.execute("INSERT INTO product (name, current_price, date) VALUES ('Клавиатура', 9000, '2025-01-30')")
cursor.execute("INSERT INTO product (name, current_price, date) VALUES ('Видеокарта', 120000, '2025-01-30')")
cursor.execute("INSERT INTO product (name, current_price, date) VALUES ('Процессор', 62000, '2025-01-30')")
cursor.execute("INSERT INTO product (name, current_price, date) VALUES ('Мат. плата', 32000, '2025-01-30')")
cursor.execute("INSERT INTO product (name, current_price, date) VALUES ('ОЗУ', 20000, '2025-01-30')")
cursor.execute("INSERT INTO product (name, current_price, date) VALUES ('БП', 12000, '2025-01-30')")
cursor.execute("INSERT INTO product (name, current_price, date) VALUES ('Аккум', 2250, '2025-01-30')")
cursor.execute("INSERT INTO product (name, current_price, date) VALUES ('VR', 95000, '2025-01-30')")
cursor.execute("INSERT INTO product (name, current_price, date) VALUES ('Джостик', 4800, '2025-01-30')")

con.commit()

cursor.execute("""CREATE TABLE storys
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                product_id INTEGER FOREGIN KEY product id,
                store_name TEXT NOT NULL,
                price REAL NOT NULL,
                change_date TEXT NOT NULL)
                """)

cursor.execute("INSERT INTO storys (product_id, store_name, price, change_date) VALUES (1, 'Магазин 1', 48000, '2025-02-02')")
cursor.execute("INSERT INTO storys (product_id, store_name, price, change_date) VALUES (1, 'Магазин 2', 50000, '2025-02-01')")
cursor.execute("INSERT INTO storys (product_id, store_name, price, change_date) VALUES (1, 'Магазин 3', 52000, '2025-01-20')")
cursor.execute("INSERT INTO storys (product_id, store_name, price, change_date) VALUES (1, 'Магазин 4', 55000, '2025-01-19')")
cursor.execute("INSERT INTO storys (product_id, store_name, price, change_date) VALUES (2, 'Магазин 5', 60000, '2025-01-18')")
cursor.execute("INSERT INTO storys (product_id, store_name, price, change_date) VALUES (2, 'Магазин 1', 70000, '2025-01-16')")
cursor.execute("INSERT INTO storys (product_id, store_name, price, change_date) VALUES (2, 'Магазин 2', 72000, '2025-01-15')")
cursor.execute("INSERT INTO storys (product_id, store_name, price, change_date) VALUES (3, 'Магазин 3', 80000, '2025-01-14')")
cursor.execute("INSERT INTO storys (product_id, store_name, price, change_date) VALUES (3, 'Магазин 4', 90000, '2025-01-11')")
cursor.execute("INSERT INTO storys (product_id, store_name, price, change_date) VALUES (3, 'Магазин 5', 100000, '2025-01s-10')")

con.commit()

def fstory(x):
    cursor.execute('''
    SELECT change_date, price, store_name
    FROM storys
    WHERE product_id = ?
    ORDER BY change_date
    ''', (x,))
    history = cursor.fetchall()
    if history:
        print(f"История изменения цен для товара с ID {x}:")
        for record in history:
            print(f"Дата: {record[0]}, Цена: {record[1]}, Магазин: {record[2]}")
    else:
        print(f"История изменения цен для товара с ID {x} отсутствует.")

def compare_prices(product_id, target_date):
    cursor.execute('SELECT current_price FROM product WHERE id = ?', (product_id,))
    current_price = cursor.fetchone()[0]

    cursor.execute('''
    SELECT price
    FROM storys
    WHERE product_id = ? AND change_date = ?
    ''', (product_id, target_date))
    target_price_top = cursor.fetchone()

    if target_price_top:
        target_price = target_price_top[0]
        difference = current_price - target_price
        if difference > 0:
            print(f"Цена выросла на {difference:.2f} руб.")
        elif difference < 0:
            print(f"Цена снизилась на {abs(difference):.2f} руб.")
        else:
            print("Цена не изменилась.")
    else:
        print(f"Данные о цене на {target_date} отсутствуют.")

fstory(1)
compare_prices(1, '2025-02-02')

con.close()