import sqlite3


async def shopping_cart_checker(user_id, value):
    conn = sqlite3.connect('core/db/data_bases/shopping_cart.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM '{user_id}' WHERE vendor_code = ?", (value,))
    row = cursor.fetchone()
    conn.close()
    return row[-2] if row else 0


async def shopping_cart_get(user_id):
    conn = sqlite3.connect('core/db/data_bases/shopping_cart.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM '{user_id}'")
    row = cursor.fetchall()
    conn.close()
    return row


async def increase_count(user_id, vendor_code):
    conn = sqlite3.connect('core/db/data_bases/shopping_cart.db')
    cursor = conn.cursor()
    cursor.execute(f"UPDATE '{user_id}' SET count = count + 1 WHERE vendor_code = ?", (vendor_code,))
    conn.commit()
    conn.close()


async def shopping_add_item(user_id, vendor_code, wine_name, wine_cost):
    conn = sqlite3.connect('core/db/data_bases/shopping_cart.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM "{user_id}" WHERE vendor_code = ?', (vendor_code,))
    data = cursor.fetchone()
    if data:
        # Если статья уже существует, увеличиваем количество на 1
        cursor.execute(f'UPDATE "{user_id}" SET count = count + 1 WHERE vendor_code = ?', (vendor_code,))
    else:
        # Если статья не существует, добавляем новую строку
        cursor.execute(f'INSERT INTO "{user_id}" (wine_name, vendor_code, count, cost) VALUES (?, ?, 1, ?)',
                       (wine_name, vendor_code, wine_cost))
    conn.commit()

    cursor.execute(f'SELECT count FROM "{user_id}" WHERE vendor_code = ?', (vendor_code,))
    updated_count = cursor.fetchone()[0]
    return updated_count


async def shopping_delete_item(user_id, vendor_code):
    conn = sqlite3.connect('core/db/data_bases/shopping_cart.db')
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM "{user_id}" WHERE vendor_code = ?', (vendor_code,))
    data = cursor.fetchone()
    if data:
        # Если статья уже существует, уменьшаем количество на 1, но не ниже 0
        cursor.execute(
            f'UPDATE "{user_id}" SET count = CASE WHEN count > 0 THEN count - 1 ELSE 0 END WHERE vendor_code = ?',
            (vendor_code,))
        cursor.execute(f'SELECT count FROM "{user_id}" WHERE vendor_code = ?', (vendor_code,))
        updated_count = cursor.fetchone()[0]
        if updated_count == 0:
            cursor.execute(f'DELETE FROM "{user_id}" WHERE vendor_code = ?', (vendor_code,))
            conn.commit()
            return 0
    else:
        # Если статья не существует, возвращаем 0
        updated_count = 0
        return updated_count
    conn.commit()

    cursor.execute(f'SELECT count FROM "{user_id}" WHERE vendor_code = ?', (vendor_code,))
    updated_count = cursor.fetchone()[0]
    return updated_count
