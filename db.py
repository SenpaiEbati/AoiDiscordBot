import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('dataconfbot.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM confbot')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()