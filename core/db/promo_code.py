import sqlite3


async def bill_promo(user_id):
    conn = sqlite3.connect('core/db/data_bases/users.db')
    cursor = conn.cursor()
    # Проверка наличия строки с id = 1
    cursor.execute(f"SELECT * FROM '{user_id}_promo' WHERE id = 1")
    promo = cursor.fetchone()
    conn.close()
    return promo
