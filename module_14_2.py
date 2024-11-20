import sqlite3

# Подключение к базе данных
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

# Создание таблицы, если её ещё нет
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# Наполнение таблицы (на случай, если она пустая)
for i in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(? ,? ,? , ?)",
                   (f"User{i}", f"example{i}@gmail.com", 10 * i, 1000))

# Обновление балансов для нечётных пользователей
for i in range(1, 11, 2):
    cursor.execute("UPDATE Users SET balance = ?", (500,))

# Удаление пользователей с id, кратными 3
for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id =?", (i,))

# Удаление пользователя с id = 6
cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

# Подсчёт общего количества пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

# Вывод среднего баланса
if total_users > 0:  # Защита от деления на ноль
    print(all_balances / total_users)
else:
    print("Нет пользователей в базе данных.")

# Закрытие соединения
connection.commit()
connection.close()
