# Mapping Specification

## Project

EDI Purchase Order Processing System

## Version

1.0

## Author

Adelopo Abdulazeez Oriyomi

## Purpose

This document defines the mapping between the ANSI X12 850 Purchase Order transaction and the internal database structure used by the EDI Purchase Order Processing System.

The purpose of the mapping is to ensure that data received from trading partners is correctly translated and stored for downstream business processing.

---

# Source Transaction

## Transaction Set

ANSI X12 850 Purchase Order

## Sample Transaction

```edi
ISA*00*          *00*          *ZZ*RETAILER      *ZZ*SUPPLIER      *240601*1200*U*00401*000000001*0*T*>~
GS*PO*RETAILER*SUPPLIER*20240601*1200*1*X*004010~
ST*850*0001~
BEG*00*SA*PO12345**20240601~
N1*BY*ABC RETAIL~
PO1*1*10*EA*15.00**VP*SKU100~
CTT*1~
SE*6*0001~
GE*1*1~
IEA*1*000000001~
```

---

# Target Database

## Table

purchase_orders

| Column Name | Data Type |
| ----------- | --------- |
| id          | INTEGER   |
| po_number   | TEXT      |
| buyer       | TEXT      |
| order_date  | TEXT      |
| quantity    | INTEGER   |
| price       | REAL      |
| sku         | TEXT      |

---

# Field Mapping

## Purchase Order Header Mapping

| EDI Segment | Element | Description           | Database Field |
| ----------- | ------- | --------------------- | -------------- |
| BEG         | BEG03   | Purchase Order Number | po_number      |
| BEG         | BEG05   | Purchase Order Date   | order_date     |

### Example

```edi
BEG*00*SA*PO12345**20240601~
```

Result:

```text
po_number = PO12345
order_date = 20240601
```

---

## Buyer Mapping

| EDI Segment | Element | Description | Database Field |
| ----------- | ------- | ----------- | -------------- |
| N1          | N102    | Buyer Name  | buyer          |

### Example

```edi
N1*BY*ABC RETAIL~
```

Result:

```text
buyer = ABC RETAIL
```

---

## Purchase Order Line Mapping

| EDI Segment | Element | Description           | Database Field |
| ----------- | ------- | --------------------- | -------------- |
| PO1         | PO102   | Quantity Ordered      | quantity       |
| PO1         | PO104   | Unit Price            | price          |
| PO1         | PO107   | Vendor Product Number | sku            |

### Example

```edi
PO1*1*10*EA*15.00**VP*SKU100~
```

Result:

```text
quantity = 10
price = 15.00
sku = SKU100
```

---

# Complete Mapping Table

| Segment | Element | Business Meaning      | Database Field |
| ------- | ------- | --------------------- | -------------- |
| BEG     | BEG03   | Purchase Order Number | po_number      |
| BEG     | BEG05   | Order Date            | order_date     |
| N1      | N102    | Buyer Name            | buyer          |
| PO1     | PO102   | Quantity              | quantity       |
| PO1     | PO104   | Unit Price            | price          |
| PO1     | PO107   | Product SKU           | sku            |

---

# Validation Rules

## Purchase Order Number

Rule:

Must not be blank.

Example:

```edi
BEG*00*SA**20240601~
```

Expected Result:

Validation Error

---

## Buyer Name

Rule:

Must not be blank.

Example:

```edi
N1*BY*~
```

Expected Result:

Validation Error

---

## Quantity

Rule:

Must be greater than zero.

Example:

```edi
PO1*1*0*EA*15.00**VP*SKU100~
```

Expected Result:

Validation Error

---

## Price

Rule:

Must be greater than zero.

Example:

```edi
PO1*1*10*EA*0**VP*SKU100~
```

Expected Result:

Validation Error

---

# Transformation Rules

| Source Value | Transformation     |
| ------------ | ------------------ |
| Quantity     | Convert to Integer |
| Price        | Convert to Float   |
| Order Date   | Store as YYYYMMDD  |
| SKU          | Store as Text      |

---

# Error Handling

## Missing Purchase Order Number

Action:

Reject transaction and write to error log.

---

## Missing Buyer

Action:

Reject transaction and write to error log.

---

## Invalid Quantity

Action:

Reject transaction and write to error log.

---

## Invalid Price

Action:

Reject transaction and write to error log.

---

# Acknowledgement Processing

Upon successful validation and storage:

1. Generate ANSI X12 997 Functional Acknowledgement.
2. Store transaction in database.
3. Archive source EDI file.
4. Record processing status.

---

# Future Enhancements

Future versions of this mapping will support:

- 810 Invoice Transactions
- 856 Advance Ship Notice (ASN)
- XML Transformations
- JSON Transformations
- PostgreSQL Storage
- Multi-Trading Partner Support

---

# Approval

| Role             | Name                       | Date |
| ---------------- | -------------------------- | ---- |
| EDI Analyst      | Adelopo Abdulazeez Oriyomi | TBD  |
| Business Analyst | TBD                        | TBD  |
| Technical Lead   | TBD                        | TBD  |
