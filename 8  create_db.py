import sqlite3

def create_database():
    conn = sqlite3.connect('gifts.db')
    cursor = conn.cursor()

    # Создаем таблицу
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gifts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            gift TEXT NOT NULL,
            price REAL NOT NULL,
            status TEXT NOT NULL
        )
    ''')

    # Вставляем данные
    gifts = [
        ('Иванов Иван', 'Книга', 500, 'не куплен'),
        ('Петров Петр', 'Часы', 1500, 'не куплен'),
        ('Сидоров Сидор', 'Наушники', 2000, 'куплен'),
        ('Кузнецова Анна', 'Плед', 800, 'куплен'),
        ('Попова Ольга', 'Флешка', 1200, 'не куплен'),
        ('Смирнов Алексей', 'Блокнот', 300, 'куплен'),
        ('Егоров Сергий', 'Кофеварка', 4000, 'не куплен'),
        ('Васильева Мария', 'Сумка', 2500, 'куплен'),
        ('Лебедева Татьяна', 'Умная колонка', 3500, 'не куплен'),
        ('Федоров Андрей', 'Игровая консоль', 20000, 'не куплен')
    ]

    cursor.executemany('''
        INSERT INTO gifts (name, gift, price, status) VALUES (?, ?, ?, ?)
    ''', gifts)

    # Сохраняем изменения
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()