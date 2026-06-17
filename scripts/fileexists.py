from pathlib import Path

file = Path("../incoming/PO850.edi")

print(file.resolve())
print(file.exists())