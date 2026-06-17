from pathlib import Path
import sqlite3

file = Path("../incoming/PO850.edi")

data = file.read_text()

segments = data.split("~")

po_number = ""
buyer = ""
order_date = ""
quantity = 0
price = 0
sku = ""

for seg in segments:

    seg = seg.strip()

    if not seg:
        continue

    parts = seg.split("*")

    if parts[0] == "BEG":
        po_number = parts[3]
        order_date = parts[5]

    elif parts[0] == "N1":
        buyer = parts[2]

    elif parts[0] == "PO1":
        quantity = int(parts[2])
        price = float(parts[4])
        sku = parts[7]

conn = sqlite3.connect("../edi.db")

cursor = conn.cursor()

cursor.execute("""
INSERT INTO purchase_orders
(po_number,buyer,order_date,quantity,price,sku)
VALUES(?,?,?,?,?,?)
""",(
    po_number,
    buyer,
    order_date,
    quantity,
    price,
    sku
))

conn.commit()

print("Order saved successfully")

conn.close()