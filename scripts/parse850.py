from pathlib import Path

file = Path("../incoming/PO850.edi")

data = file.read_text()

segments = data.split("~")

po_number = ""
buyer = ""

for seg in segments:

    seg = seg.strip()

    if not seg:
        continue

    parts = seg.split("*")

    if parts[0] == "BEG":
        po_number = parts[3]

    elif parts[0] == "N1":
        buyer = parts[2]

print("PO:", po_number)
print("Buyer:", buyer)