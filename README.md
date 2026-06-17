# EDI Purchase Order Processing System

## Project Overview

This project demonstrates a simple Electronic Data Interchange (EDI) Purchase Order Processing System developed using Python and SQLite.

The solution receives an ANSI X12 850 Purchase Order, extracts business information, stores the data in a database, generates a 997 Functional Acknowledgement, and archives processed files.

## Business Scenario

A retailer sends an EDI 850 Purchase Order to a supplier.

The application:

1. Receives the EDI file.
2. Parses EDI segments.
3. Extracts purchase order information.
4. Stores transaction data in a database.
5. Generates a 997 Acknowledgement.
6. Archives processed files.
7. Logs processing errors.

## Technologies Used

- Python 3
- SQLite
- Git
- GitHub
- Bots EDI Translator

## EDI Transactions

### Inbound

- ANSI X12 850 Purchase Order

### Outbound

- ANSI X12 997 Functional Acknowledgement

## Project Structure

```text
edi-lab/
│
├── archive/
├── incoming/
├── outgoing/
├── reports/
├── scripts/
│   ├── create_db.py
│   ├── process850.py
│   ├── view_orders.py
│   └── generate997.py
│
├── edi.db
├── README.md
└── .gitignore
```

## Sample EDI 850

```edi
BEG*00*SA*PO12345**20240601~
N1*BY*ABC RETAIL~
PO1*1*10*EA*15.00**VP*SKU100~
```

## Sample Output

```text
PURCHASE ORDER
----------------------------------------
PO Number : PO12345
Buyer     : ABC RETAIL
Order Date: 20240601
Quantity  : 10
Price     : 15.00
SKU       : SKU100
```

## Skills Demonstrated

- EDI Processing
- ANSI X12 Standards
- Data Mapping
- Python Automation
- Database Integration
- Error Handling
- Troubleshooting
- System Integration

## Future Enhancements

- PostgreSQL Integration
- Trading Partner Management
- AS2 Communication
- XML and JSON Transformations
- Apache NiFi Integration
- Automated Monitoring Dashboard

## Author

Adelopo Abdulazeez Oriyomi
