# SQAnalytics Schema V1

## Table: qr_codes

| Column | Data Type | Description |
|----------|----------|----------|
| qr_id | UUID | Primary Key |
| short_code | VARCHAR(20) | Redirect Code |
| title | VARCHAR(255) | QR Name |
| destination_url | TEXT | Redirect Destination |
| status | VARCHAR(20) | active/inactive |
| created_at | TIMESTAMP | Creation Timestamp |
| updated_at | TIMESTAMP | Last Updated Timestamp |

## Relationships

Currently none.

Future:

qr_codes
1
|
|
many
scan_events