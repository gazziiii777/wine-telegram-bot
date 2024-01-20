import sqlite3


async def bill_promo(user_id):
    conn = sqlite3.connect('core/db/data_bases/users.db')
    cursor = conn.cursor()
    # Проверка наличия строки с id = 1
    cursor.execute(f"SELECT * FROM '{user_id}_promo' WHERE id = 1")
    promo = cursor.fetchone()
    conn.close()
    return promo


async def check_promo(user_id, promo_code):
    conn = sqlite3.connect('core/db/data_bases/promo.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM promo")
    rows = cursor.fetchall()
    for row in rows:
        if promo_code == row[1]:
            return await promo_wind(user_id, row)
        else:
            return 0
    conn.close()


async def promo_wind(user_id, promo_code_row):
    conn = sqlite3.connect('core/db/data_bases/users.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE '{user_id}_promo' SET promo_code = ? WHERE id = 1", (promo_code_row[2],))
    conn.commit()
    conn.close()
    return f'Промокод: <b>{promo_code_row[1]}</b> на скидку в {int(100 * float(promo_code_row[2]))} % применен'


async def add_new_promo(promo_code_name, promo_code_value):
    conn = sqlite3.connect('core/db/data_bases/promo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM promo WHERE promo_code = ?", (promo_code_name,))
    row = cursor.fetchone()
    if row:
        conn.close()
        return 0
    else:
        cursor.execute("INSERT INTO promo (promo_code, value) VALUES (?, ?)", (promo_code_name, promo_code_value))
    conn.commit()
    conn.close()
    return f"Промокод {promo_code_name} добавлен, доющий скидку в {int(100 * float(promo_code_value))} %"
