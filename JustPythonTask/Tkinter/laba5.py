import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

class PriceTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Трекер цен товаров")
        self.root.geometry("800x600")
        
        # Подключение к базе данных
        self.conn = sqlite3.connect('price_tracker.db')
        self.cursor = self.conn.cursor()
        
        # Создание таблиц
        self.create_tables()
        
        # Заполнение тестовыми данными (если таблицы пустые)
        self.insert_sample_data()
        
        # Создание интерфейса
        self.create_widgets()
    
    def create_tables(self):
        """Создание таблиц в базе данных"""
        # Таблица товаров
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                current_price REAL NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        
        # Таблица истории цен
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS price_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                store_name TEXT NOT NULL,
                price REAL NOT NULL,
                change_date TEXT NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products (id)
            )
        ''')
        
        self.conn.commit()
    
    def insert_sample_data(self):
        """Заполнение базы данных тестовыми данными"""
        # Проверяем, есть ли уже данные в таблице товаров
        self.cursor.execute("SELECT COUNT(*) FROM products")
        count = self.cursor.fetchone()[0]
        
        if count == 0:
            # Добавляем товары
            products = [
                ('Ноутбук', 50000, '2025-01-30'),
                ('Смартфон', 30000, '2025-01-30'),
                ('Телевизор', 45000, '2025-01-30'),
                ('Наушники', 5000, '2025-01-30'),
                ('Планшет', 25000, '2025-01-30'),
                ('Фотоаппарат', 35000, '2025-01-30'),
                ('Игровая консоль', 40000, '2025-01-30'),
                ('Монитор', 20000, '2025-01-30'),
                ('Клавиатура', 1500, '2025-01-30'),
                ('Мышь', 800, '2025-01-30'),
                ('Принтер', 12000, '2025-01-30'),
                ('Сканер', 9000, '2025-01-30'),
                ('Колонки', 3500, '2025-01-30'),
                ('Роутер', 4000, '2025-01-30'),
                ('Внешний жесткий диск', 6000, '2025-01-30')
            ]
            
            self.cursor.executemany(
                "INSERT INTO products (name, current_price, date) VALUES (?, ?, ?)",
                products
            )
            
            # Добавляем историю цен для 5 товаров в 5 магазинах
            stores = ['Магазин 1', 'Магазин 2', 'Магазин 3', 'Магазин 4', 'Магазин 5']
            
            for product_id in range(1, 6):
                for store in stores:
                    base_price = products[product_id-1][1]
                    for i in range(2):  # 2 изменения цены для каждого магазина
                        price_change = ( i + 1 ) * 500 * ( -1 if i % 2 else 1 )
                        new_price = base_price + price_change
                        date = f'2025-0{1+i}-{10+i}'
                        
                        self.cursor.execute(
                            "INSERT INTO price_history (product_id, store_name, price, change_date) VALUES (?, ?, ?, ?)",
                            (product_id, store, new_price, date)
                        )
            
            self.conn.commit()
    
    def create_widgets(self):
        """Создание элементов интерфейса"""
        # Основные вкладки
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=BOTH, expand = True)
        
        # Вкладка просмотра товаров
        self.products_tab = Frame(self.notebook)
        self.notebook.add(self.products_tab, text = "Товары")
        self.create_products()
        
        # Вкладка истории цен
        self.history_tab = Frame(self.notebook)
        self.notebook.add(self.history_tab, text = "История цен")
        self.create_history()
        
        # Вкладка сравнения цен
        self.compare_tab = Frame(self.notebook)
        self.notebook.add(self.compare_tab, text = "Сравнение цен")
        self.create_compare()
    
    def create_products(self):
        """Создание вкладки с товарами"""
        # Таблица товаров
        columns = ("id", "name", "price", "date")
        self.products_tree = ttk.Treeview(
            self.products_tab, columns = columns, show = "headings"
        )
        
        for col in columns:
            self.products_tree.heading(col, text = col.capitalize())
            self.products_tree.column(col, width = 100)
        
        self.products_tree.pack(fill = BOTH, expand = True, padx = 5, pady = 5)
        
        # Кнопка обновления
        Button(
            self.products_tab, text="Обновить список", 
            command=self.update_products_list
        ).pack(pady=5)
        
        # Заполняем таблицу
        self.update_products_list()
    
    def update_products_list(self):
        """Обновление списка товаров"""
        for item in self.products_tree.get_children():
            self.products_tree.delete(item)
            
        self.cursor.execute("SELECT * FROM products ORDER BY name")
        for row in self.cursor.fetchall():
            self.products_tree.insert("", END, values = row)
    
    def create_history(self):
        """Создание вкладки с историей цен"""
        # Выбор товара
        Label(self.history_tab, text = "Выберите товар:").pack(pady = 5)
        
        self.product_var = StringVar()
        self.product_combobox = ttk.Combobox(
            self.history_tab, textvariable = self.product_var, state = "readonly"
        )
        self.product_combobox.pack(pady = 5)
        
        # Заполняем комбобокс товарами
        self.update_products_combobox()
        
        # Таблица истории цен
        columns = ("store", "price", "date")
        self.history_tree = ttk.Treeview(
            self.history_tab, columns = columns, show = "headings"
        )
        
        for col in columns:
            self.history_tree.heading(col, text = col.capitalize())
            self.history_tree.column(col, width = 100)
        
        self.history_tree.pack(fill = BOTH, expand = True, padx = 5, pady = 5)
        
        # Кнопка показа истории
        Button(
            self.history_tab, text="Показать историю", 
            command=self.show_price_history
        ).pack(pady=5)
    
    def update_products_combobox(self):
        """Обновление списка товаров в комбобоксе"""
        self.cursor.execute("SELECT id, name FROM products ORDER BY name")
        products = self.cursor.fetchall()
        self.product_combobox['values'] = [f"{p[0]}. {p[1]}" for p in products]
        if products:
            self.product_combobox.current(0)
    
    def show_price_history(self):
        """Отображение истории цен для выбранного товара"""
        selection = self.product_var.get()
        if not selection:
            messagebox.showwarning("Ошибка!!!", "Выберите товар")
            return
        
        product_id = int(selection.split('.')[0])
        
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)
            
        self.cursor.execute('''
            SELECT store_name, price, change_date 
            FROM price_history 
            WHERE product_id = ? 
            ORDER BY change_date DESC
        ''', (product_id,))
        
        for row in self.cursor.fetchall():
            self.history_tree.insert("", END, values = row)
    
    def create_compare(self):
        """Создание вкладки сравнения цен"""
        # Выбор товара
        Label(self.compare_tab, text="Выберите товар:").pack( pady = 5 )
        
        self.compare_product_var = StringVar()
        self.compare_product_combobox = ttk.Combobox(
            self.compare_tab, textvariable=self.compare_product_var, state="readonly"
        )
        self.compare_product_combobox.pack( pady = 5 )
        
        # Заполняем комбобокс товарами
        self.update_compare_products_combobox()
        
        # Выбор даты для сравнения
        Label(self.compare_tab, text="Выберите дату для сравнения (ГГГГ-ММ-ДД):").pack(pady=5)
        
        self.compare_date_var = StringVar()
        self.compare_date_entry = Entry(
            self.compare_tab, textvariable = self.compare_date_var
        )
        self.compare_date_entry.pack( pady = 5 )
        self.compare_date_entry.insert(0, "2025-01-30")
        
        # Кнопка сравнения
        Button(
            self.compare_tab, text="Сравнить цены", 
            command=self.compare_prices
        ).pack( pady = 10 )
        
        # Поле для вывода результата
        self.compare_result = Text(
            self.compare_tab, height = 10, width = 80, state = DISABLED
        )
        self.compare_result.pack(pady = 5, padx = 5, fill = BOTH, expand = True)
    
    def update_compare_products_combobox(self):
        """Обновление списка товаров в комбобоксе сравнения"""
        self.cursor.execute("SELECT id, name FROM products ORDER BY name")
        products = self.cursor.fetchall()
        self.compare_product_combobox['values'] = [f"{p[0]}. {p[1]}" for p in products]
        if products:
            self.compare_product_combobox.current(0)
    
    def compare_prices(self):
        """Сравнение текущей цены с ценой на указанную дату"""
        selection = self.compare_product_var.get()
        if not selection:
            messagebox.showwarning("Ошибка", "Выберите товар")
            return
        
        compare_date = self.compare_date_var.get()
        try:
            datetime.strptime(compare_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showwarning("Ошибка", "Некорректный формат даты. Используйте ГГГГ-ММ-ДД")
            return
        
        product_id = int(selection.split('.')[0])
        
        # Получаем текущую цену
        self.cursor.execute(
            "SELECT name, current_price FROM products WHERE id = ?", 
            (product_id,)
        )
        product_name, current_price = self.cursor.fetchone()
        
        # Получаем цену на указанную дату
        self.cursor.execute('''
            SELECT price 
            FROM price_history 
            WHERE product_id = ? AND change_date <= ?
            ORDER BY change_date DESC
            LIMIT 1
        ''', (product_id, compare_date))
        
        result = self.cursor.fetchone()
        if not result:
            messagebox.showwarning("Ошибка", f"Нет данных о ценах на {compare_date}")
            return
        
        old_price = result[0]
        difference = current_price - old_price
        
        # Формируем результат
        self.compare_result.config(state=NORMAL)
        self.compare_result.delete(1.0, END)
        
        self.compare_result.insert(END, f"Товар: {product_name}\n")
        self.compare_result.insert(END, f"Текущая цена: {current_price:.2f} руб.\n")
        self.compare_result.insert(END, f"Цена на {compare_date}: {old_price:.2f} руб.\n")
        self.compare_result.insert(END, "\n")
        
        if difference > 0:
            self.compare_result.insert(END, f"Цена выросла на {difference:.2f} руб.")
        elif difference < 0:
            self.compare_result.insert(END, f"Цена снизилась на {abs(difference):.2f} руб.")
        else:
            self.compare_result.insert(END, "Цена не изменилась.")
        
        self.compare_result.config(state=DISABLED)
    
    def __del__(self):
        self.conn.close()

root = Tk()
app = PriceTrackerApp(root)
root.mainloop()