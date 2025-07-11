# Cloud Programming Project – AWS S3 + Python (Boto3)

## Student Details
- **Name**: Your Name
- **PRN**: 23BCE0000 (replace with your actual PRN)
- **Technology Used**: Python, AWS S3, Boto3, Watchdog
- **Level**: Advanced (5 Levels Completed)

---

## Project Overview

This project demonstrates a full lifecycle of cloud-based file storage operations using **AWS S3** and **Python**, with features progressing from basic to advanced levels:

|         Level              |            Description            |
|----------------------------|-----------------------------------|
| 1 | Basic file operations with S3 (upload, list, delete, move) |
| 2 | File type validation, error handling, verbose logging      |
| 3 | Automatic/scheduled backups of local folders               |
| 4 | Real-time file sync using change detection                 |
| 5 | Zipping and versioned uploads to S3                        |

---

## Folder Structure
cloud_s3_project/
├── backup_files/ # For scheduled backups
├── sync_folder/ # For real-time monitoring
├── zip_source/ # Source files to be zipped
├── create_bucket.py
├── upload_file.py
├── list_files.py
├── modify_and_upload.py
├── move_jpg_files.py
├── validated_upload.py
├── auto_backup.py
├── auto_sync.py
├── enable_versioning.py
├── zip_and_upload.py
├── file_sync.log
├── s3_upload.log
├── auto_backup.log
└── README.md


---

## Tools & Libraries

- **boto3** – AWS SDK for Python
- **watchdog** – Detects file changes in folders
- **zipfile** – Built-in Python module for zipping files
- **logging** – Tracks system behavior and errors

---

## Setup Instructions

1. **Install required packages**:
   ```bash
   pip install boto3 watchdog

2. **Configure AWS credentials**:
   ```bash
   aws configure

3. **Run each Python file for the respective functionality**:

- **Create bucket**: create_bucket.py
- **Upload file**: upload_file.py, etc.

**Bucket Details**
- **Bucket Name**: Must be your PRN number (e.g., 24030142004)

- **Versioning**: Enabled using enable_versioning.py

**Folder Structure in S3**:
- **pictures/** – Moved image files
- **backups/** – Scheduled backup uploads
- **synced/** – Auto-synced files
- **zips/** – Uploaded ZIPs with versioning

**Features Demonstrated**
- Upload, list, delete, and move files in S3
- Filter file types (.pdf, .jpeg, .mpeg, .doc, .txt)
- Log activities and handle exceptions gracefully
- Auto-backup using timestamps
- Watch folders for file changes
- Versioned uploads of zipped data

**References**
- ***https://boto3.amazonaws.com/v1/documentation/api/latest/index.html***

**Conclusion**
This project showcases how cloud storage operations can be automated and enhanced using Python. It combines real-time monitoring, validation, error handling, and version control for a complete cloud-based file management solution.#   P r o g r a m m i n g - S 3 - b a s e d - a p p l i c a t i o n - - - B a c k u p - R e c o v e r y - A g e n t - S o f t w a r e  
 