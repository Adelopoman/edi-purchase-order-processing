# EDI Troubleshooting Guide

## Project

EDI Purchase Order Processing System

## Version

1.0

## Author

Adelopo Abdulazeez Oriyomi

## Purpose

This document provides troubleshooting procedures for diagnosing and resolving issues encountered during EDI transaction processing.

The guide serves as an operational reference for EDI Analysts, EDI Support Engineers, Integration Engineers, and System Administrators.

---

# Incident Management Process

When an EDI issue is reported:

1. Identify the affected transaction.
2. Determine the processing stage where the failure occurred.
3. Review logs and transaction data.
4. Identify root cause.
5. Apply corrective action.
6. Retest transaction.
7. Document resolution.

---

# Transaction Processing Flow

```text
Trading Partner
      |
      V
Inbound EDI File
      |
      V
Validation
      |
      V
Parsing
      |
      V
Database Storage
      |
      V
997 Acknowledgement
      |
      V
Archive
```

---

# Common Issues and Resolutions

## Issue 1: EDI File Not Found

### Symptoms

- Processing job fails.
- Incoming folder is empty.
- No transaction appears in the database.

### Root Causes

- Trading partner did not transmit the file.
- File was accidentally deleted.
- Incorrect file location configured.

### Investigation Steps

Verify file exists:

```cmd
dir incoming
```

Verify application path configuration.

### Resolution

- Request retransmission from trading partner.
- Restore file from backup if available.
- Correct file path configuration.

---

## Issue 2: Missing Purchase Order Number

### Symptoms

- Validation failure.
- Transaction rejected.
- Error recorded in log.

### Example

```edi
BEG*00*SA**20240601~
```

### Root Cause

BEG03 element is empty.

### Resolution

- Reject transaction.
- Notify trading partner.
- Request corrected document.

---

## Issue 3: Missing Buyer Information

### Symptoms

- Buyer field is blank.
- Transaction cannot be processed.

### Example

```edi
N1*BY*~
```

### Root Cause

N102 element missing.

### Resolution

- Reject transaction.
- Request corrected file.

---

## Issue 4: Invalid Quantity

### Symptoms

- Quantity equals zero.
- Quantity is non-numeric.

### Example

```edi
PO1*1*0*EA*15.00**VP*SKU100~
```

### Root Cause

Business validation failure.

### Resolution

- Reject transaction.
- Notify trading partner.

---

## Issue 5: Invalid Unit Price

### Symptoms

- Unit price is missing.
- Unit price equals zero.

### Example

```edi
PO1*1*10*EA*0**VP*SKU100~
```

### Resolution

- Reject transaction.
- Request corrected transaction.

---

## Issue 6: Invalid EDI Segment

### Symptoms

- Parser fails.
- Unexpected segment encountered.

### Example

```edi
ABC*INVALID*SEGMENT~
```

### Root Cause

Unsupported segment.

### Resolution

- Review implementation guide.
- Update mapping if necessary.
- Reject invalid transaction.

---

## Issue 7: Empty EDI File

### Symptoms

- No transaction processed.
- Parser returns empty result.

### Investigation

Verify file size:

```cmd
dir incoming
```

### Resolution

- Request file retransmission.
- Validate file generation process.

---

# Database Issues

## Issue 8: Database Connection Failure

### Symptoms

- Records not inserted.
- Database errors displayed.

### Example Error

```text
sqlite3.OperationalError: unable to open database file
```

### Investigation

Verify database exists:

```cmd
dir edi.db
```

### Resolution

- Recreate database.
- Verify permissions.
- Verify connection string.

---

## Issue 9: Duplicate Purchase Orders

### Symptoms

- Same PO processed multiple times.

### Root Cause

Trading partner retransmitted document.

### Resolution

- Implement duplicate detection.
- Compare Purchase Order Number before insert.

### Recommended Check

```sql
SELECT *
FROM purchase_orders
WHERE po_number='PO12345';
```

---

# Acknowledgement Issues

## Issue 10: 997 Acknowledgement Not Generated

### Symptoms

- Trading partner reports missing ACK.

### Investigation

Verify output folder:

```cmd
dir outgoing
```

Verify acknowledgement generation script executed.

### Resolution

- Reprocess transaction.
- Regenerate 997 ACK.

---

## Issue 11: Invalid 997 Acknowledgement

### Symptoms

- Trading partner rejects ACK.

### Root Cause

Incorrect AK segments.

### Investigation

Validate:

```edi
AK1
AK9
SE
```

segments.

### Resolution

Correct acknowledgement mapping.

---

# File Archive Issues

## Issue 12: File Not Archived

### Symptoms

- File remains in incoming directory.
- Duplicate processing occurs.

### Investigation

Review archive process logs.

### Resolution

Verify:

```python
shutil.move()
```

executed successfully.

---

# Logging and Monitoring

## Error Log Location

```text
reports/errors.log
```

## Common Log Entries

```text
Missing Purchase Order Number
Missing Buyer
Invalid Quantity
Invalid Price
Database Connection Error
```

---

# Root Cause Analysis Template

## Incident Number

INC-XXXX

## Date

YYYY-MM-DD

## Transaction Type

850 Purchase Order

## Description

Brief description of issue.

## Root Cause

Underlying cause identified.

## Resolution

Actions taken to resolve issue.

## Preventive Action

Steps implemented to prevent recurrence.

---

# Escalation Matrix

| Severity | Description                    | Action                           |
| -------- | ------------------------------ | -------------------------------- |
| Critical | System unavailable             | Immediate escalation             |
| High     | Transaction processing failure | Escalate within 1 hour           |
| Medium   | Partial functionality issue    | Escalate within 4 hours          |
| Low      | Minor issue                    | Resolve during normal operations |

---

# Monitoring Checklist

Daily operational checks:

- Verify incoming folder processing.
- Verify database inserts.
- Verify 997 acknowledgements generated.
- Verify archive folder updates.
- Review error logs.
- Review failed transactions.
- Confirm trading partner connectivity.

---

# Best Practices

1. Validate all inbound transactions.
2. Log all processing failures.
3. Archive processed files.
4. Maintain mapping documentation.
5. Monitor acknowledgement generation.
6. Implement duplicate transaction detection.
7. Maintain transaction audit trails.
8. Test all mapping changes before deployment.

---

# Approval

| Role             | Name               | Status   |
| ---------------- | ------------------ | -------- |
| EDI Analyst      | Abdulazeez Adelopo | Approved |
| Support Engineer | TBD                | Pending  |
| Technical Lead   | TBD                | Pending  |
