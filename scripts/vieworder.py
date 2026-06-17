import sqlite3

conn = sqlite3.connect("../edi.db")

cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM purchase_orders
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()