import pymysql

DB_CONFIG = {
    'host': 'sql7.freesqldatabase.com',
    'port': 3306,
    'user': 'sql7779677',
    'password': 'PAb8wZXsRR',
    'database': 'sql7779677'
}

try:
    connection = pymysql.connect(**DB_CONFIG)
    print("Успешное подключение к базе")
    connection.close()
except Exception as e:
    print("Ошибка подключения:", e)
