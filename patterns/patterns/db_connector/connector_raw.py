import sqlite3
from sqlite3 import Connection, Cursor

from patterns.query_object import query_raw

if __name__ == "__main__":

    # подключение к БД
    connection: Connection = sqlite3.connect(':memory:')
    cursor: Cursor = connection.cursor()

    # Выполенение запросов
    cursor.executescript(query_raw.create_table_script)
    cursor.executemany(query_raw.insert_query, query_raw.data)
    cursor.execute(query_raw.select_query)

    # получение данных
    row: list[str, str] = cursor.fetchone()
    print(row)  # ('John Doe', 'john@example.com')

    cursor.execute(query_raw.drop_table_script)