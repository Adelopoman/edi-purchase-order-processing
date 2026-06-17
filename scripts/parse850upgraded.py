from pathlib import Path

file = Path("../incoming/PO850.edi")

data = file.read_text()

segments = data.split("~")

po_number = ""
order_date = ""
buyer = ""
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
        quantity = parts[2]
        price = parts[4]
        sku = parts[7]

print("\nPURCHASE ORDER")
print("-" * 40)
print("PO Number :", po_number)
print("Buyer     :", buyer)
print("Order Date:", order_date)
print("Quantity  :", quantity)
print("Price     :", price)
print("SKU       :", sku)