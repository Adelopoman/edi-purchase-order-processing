from pathlib import Path

file = Path("../incoming/PO850.edi")

data = file.read_text()

segments = data.split("~")

for segment in segments:
    print(repr(segment))