########## Lab work №6 (05.12.2024) ##########


# Task 1

# Option 1
import sqlite3

conn = sqlite3.connect("presents.db")
cursor = conn.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS presents (
    id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    gift_name TEXT NOT NULL,
    cost REAL NOT NULL,
    status TEXT NOT NULL
)
"""
)

presents_data = [
    ("Светлана", "Сертификат в спа", 3500, "куплен"),
    ("Михаил", "Виниловая пластинка", 2700, "куплен"),
    ("Татьяна", "Набор для рукоделия", 2400, "не куплен"),
    ("Алексей", "Набор для рыбалки", 2300, "не куплен"),
    ("Людмила", "Гаджет", 2500, "куплен"),
    ("Виктория", "Гаджет", 2200, "куплен"),
    ("Вячеслав", "Конструктор", 2100, "не куплен"),
    ("Роман", "Билеты на концерт", 4000, "не куплен"),
    ("Дамир", "Игровой набор", 3800, "куплен"),
    ("Александр", "Игрушка", 1500, "не куплен"),
]

cursor.executemany(
    "INSERT INTO presents (full_name, gift_name, cost, status) VALUES (?, ?, ?, ?)",
    presents_data,
)

conn.commit()

cursor.execute("SELECT * FROM presents")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
