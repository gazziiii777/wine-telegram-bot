import sqlite3


async def assortment_wine(wine):
    conn = sqlite3.connect('core/db/data_bases/wine.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {wine}")
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    return rows
