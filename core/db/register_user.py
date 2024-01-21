import sqlite3


async def register_user(user_id, username):
    conn = sqlite3.connect('core/db/data_bases/users.db')
    cursor = conn.cursor()

    # Запрос, чтобы проверить наличие ID в колонке
    query = "SELECT * FROM users WHERE user_id = ? AND username = ?"
    cursor.execute(query, (user_id, username,))
    result = cursor.fetchall()

    if result:
        print("ID найден в таблице.")
    else:
        print("ID не найден в таблице. Добавление ID в таблицу...")
        insert_query = "INSERT INTO users (user_id, username) VALUES (?, ?)"
        cursor.execute(insert_query, (user_id, username))
        conn.commit()
        print("ID успешно добавлен в таблицу.")

    conn.close()


async def creating_a_shopping_cart(user_id):
    conn = sqlite3.connect('core/db/data_bases/shopping_cart.db')
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS "{user_id}"
                      (id INTEGER PRIMARY KEY, wine_name TEXT, vendor_code TEXT, count INTEGER, cost INTEGER)''')

    conn.close()


async def creating_user_promo_code(user_id):
    conn = sqlite3.connect('core/db/data_bases/users.db')
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS "{user_id}_promo"
                      (id INTEGER PRIMARY KEY, promo_code TEXT)''')
    # Проверка наличия строки с id = 1
    cursor.execute(f"SELECT * FROM '{user_id}_promo' WHERE id = 1")
    row = cursor.fetchone()
    if row:
        # cursor.execute(f"UPDATE \"{user_id}_promo\" SET promo_code = ? WHERE id = 1", (0,))
        # conn.commit()
        conn.close()
    else:
        # Если строки с id = 1 нет, то выполняем добавление
        cursor.execute(f"INSERT INTO \"{user_id}_promo\" (promo_code) VALUES (?)", (0,))
        conn.commit()

    conn.close()


async def profile_info(user_id):
    conn = sqlite3.connect('core/db/data_bases/users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        list_row = list(row)
        if list_row[1] == str(user_id):
            if None in list_row:
                for i in range(len(list_row)):
                    if list_row[i] is None:
                        list_row[i] = "Пусто"
                return list_row
            else:
                return list_row
