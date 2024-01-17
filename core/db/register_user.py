import sqlite3


async def register_user(user_id):
    conn = sqlite3.connect('core/db/data_bases/users.db')
    cursor = conn.cursor()
    # Запрос, чтобы проверить наличие ID в колонке
    query = "SELECT * FROM users WHERE user_id = ?"
    cursor.execute(query, (user_id,))
    result = cursor.fetchall()

    if result:
        print("ID найден в таблице.")
    else:
        print("ID не найден в таблице. Добавление ID в таблицу...")
        insert_query = "INSERT INTO users (user_id) VALUES (?)"
        cursor.execute(insert_query, (user_id,))
        conn.commit()
        print("ID успешно добавлен в таблицу.")

    conn.close()
