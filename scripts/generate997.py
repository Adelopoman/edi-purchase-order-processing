from pathlib import Path

ack = """ISA*00*ACK~
GS*FA~
ST*997*0001~
AK1*PO~
AK9*A*1*1*1~
SE*5*0001~
GE*1*1~
IEA*1*1~
"""

output = Path("../outgoing/997_ACK.edi")

output.write_text(ack)

print("997 ACK generated")