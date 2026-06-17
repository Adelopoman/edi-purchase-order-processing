import sqlite3

conn = sqlite3.connect("../edi.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS purchase_orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    po_number TEXT,
    buyer TEXT,
    order_date TEXT,
    quantity INTEGER,
    price REAL,
    sku TEXT
)
""")

conn.commit()

print("Database created successfully")

conn.close()