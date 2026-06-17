# Test Cases

## Project

EDI Purchase Order Processing System

## Version

1.0

## Author

Adelopo Abdulazeez Oriyomi

## Purpose

This document defines the test cases used to validate the EDI Purchase Order Processing System.

The objective is to verify that incoming ANSI X12 850 Purchase Orders are correctly processed, validated, stored, acknowledged, and archived.

---

# Test Environment

| Item                 | Value                          |
| -------------------- | ------------------------------ |
| Operating System     | Windows 11                     |
| Language             | Python 3                       |
| Database             | SQLite                         |
| EDI Standard         | ANSI X12                       |
| Inbound Transaction  | 850 Purchase Order             |
| Outbound Transaction | 997 Functional Acknowledgement |

---

# Test Summary

| Category              | Total Cases |
| --------------------- | ----------- |
| Positive Tests        | 6           |
| Negative Tests        | 8           |
| Database Tests        | 3           |
| Acknowledgement Tests | 2           |
| Archive Tests         | 2           |
| Total                 | 21          |

---

# Positive Test Cases

## TC-001 Valid Purchase Order

### Objective

Verify that a valid EDI 850 file is successfully processed.

### Input

```edi
BEG*00*SA*PO12345**20240601~
N1*BY*ABC RETAIL~
PO1*1*10*EA*15.00**VP*SKU100~
```

### Expected Result

- Purchase Order parsed successfully
- Data stored in database
- 997 ACK generated
- File archived

### Status

Pass

---

## TC-002 Extract Purchase Order Number

### Objective

Verify Purchase Order Number extraction.

### Input

```edi
BEG*00*SA*PO12345**20240601~
```

### Expected Result

```text
PO Number = PO12345
```

### Status

Pass

---

## TC-003 Extract Buyer Information

### Objective

Verify Buyer Name extraction.

### Input

```edi
N1*BY*ABC RETAIL~
```

### Expected Result

```text
Buyer = ABC RETAIL
```

### Status

Pass

---

## TC-004 Extract Quantity

### Objective

Verify Quantity extraction.

### Input

```edi
PO1*1*10*EA*15.00**VP*SKU100~
```

### Expected Result

```text
Quantity = 10
```

### Status

Pass

---

## TC-005 Extract Unit Price

### Objective

Verify Price extraction.

### Input

```edi
PO1*1*10*EA*15.00**VP*SKU100~
```

### Expected Result

```text
Price = 15.00
```

### Status

Pass

---

## TC-006 Extract SKU

### Objective

Verify Product SKU extraction.

### Input

```edi
PO1*1*10*EA*15.00**VP*SKU100~
```

### Expected Result

```text
SKU = SKU100
```

### Status

Pass

---

# Negative Test Cases

## TC-007 Missing Purchase Order Number

### Objective

Verify validation of missing PO Number.

### Input

```edi
BEG*00*SA**20240601~
```

### Expected Result

- Validation error generated
- Transaction rejected
- Error written to log

### Status

Pass

---

## TC-008 Missing Buyer Name

### Objective

Verify validation of missing Buyer.

### Input

```edi
N1*BY*~
```

### Expected Result

- Validation error
- Transaction rejected

### Status

Pass

---

## TC-009 Missing Quantity

### Objective

Verify validation of missing quantity.

### Input

```edi
PO1*1**EA*15.00**VP*SKU100~
```

### Expected Result

- Validation error
- Transaction rejected

### Status

Pass

---

## TC-010 Quantity Equals Zero

### Objective

Verify quantity validation.

### Input

```edi
PO1*1*0*EA*15.00**VP*SKU100~
```

### Expected Result

- Validation error
- Transaction rejected

### Status

Pass

---

## TC-011 Missing Price

### Objective

Verify missing price validation.

### Input

```edi
PO1*1*10*EA***VP*SKU100~
```

### Expected Result

- Validation error

### Status

Pass

---

## TC-012 Price Equals Zero

### Objective

Verify price validation.

### Input

```edi
PO1*1*10*EA*0**VP*SKU100~
```

### Expected Result

- Validation error

### Status

Pass

---

## TC-013 Invalid Segment

### Objective

Verify invalid segment handling.

### Input

```edi
ABC*INVALID*SEGMENT~
```

### Expected Result

- Segment rejected
- Error logged

### Status

Pass

---

## TC-014 Empty File

### Objective

Verify empty file handling.

### Input

```text

```

### Expected Result

- Transaction rejected
- Error logged

### Status

Pass

---

# Database Test Cases

## TC-015 Database Insert

### Objective

Verify successful database insertion.

### Expected Result

```sql
SELECT * FROM purchase_orders;
```

Returns newly inserted record.

### Status

Pass

---

## TC-016 Data Integrity Validation

### Objective

Verify stored values match source EDI transaction.

### Expected Result

Database values equal EDI values.

### Status

Pass

---

## TC-017 Duplicate Transaction Handling

### Objective

Verify duplicate Purchase Orders are identified.

### Input

Same Purchase Order processed twice.

### Expected Result

- Duplicate detected
- Warning generated

### Status

Future Enhancement

---

# Acknowledgement Test Cases

## TC-018 Generate 997 Acknowledgement

### Objective

Verify generation of outbound 997 ACK.

### Expected Result

```edi
AK9*A*1*1*1~
```

Generated successfully.

### Status

Pass

---

## TC-019 Acknowledgement File Creation

### Objective

Verify ACK file exists in outgoing directory.

### Expected Result

```text
outgoing/997_ACK.edi
```

File exists.

### Status

Pass

---

# Archive Test Cases

## TC-020 Archive Processed File

### Objective

Verify processed file moves to archive.

### Expected Result

```text
archive/PO850.edi
```

File exists.

### Status

Pass

---

## TC-021 Remove File From Incoming Folder

### Objective

Verify incoming directory is cleared after processing.

### Expected Result

```text
incoming/
```

Folder is empty.

### Status

Pass

---

# Defect Severity Levels

| Severity | Description                    |
| -------- | ------------------------------ |
| Critical | Processing cannot continue     |
| High     | Major functionality impacted   |
| Medium   | Partial functionality affected |
| Low      | Cosmetic or minor issue        |

---

# Exit Criteria

Testing is considered complete when:

- All positive test cases pass.
- All critical defects are resolved.
- Database records are accurate.
- 997 Acknowledgements are generated correctly.
- Files are archived successfully.
- Error handling behaves as expected.

---

# Approval

| Role           | Name               | Status   |
| -------------- | ------------------ | -------- |
| EDI Analyst    | Abdulazeez Adelopo | Approved |
| QA Analyst     | TBD                | Pending  |
| Technical Lead | TBD                | Pending  |
