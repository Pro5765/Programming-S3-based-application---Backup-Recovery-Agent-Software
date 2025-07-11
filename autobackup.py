import boto3
import os
import time
import logging
from datetime import datetime

logging.basicConfig(
    filename='auto_backup.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

bucket_name = '24030142004'
backup_folder = 'backups/'
local_folder = 'backup_files/'
allowed_extensions = ['.pdf', '.jpeg', '.jpg', '.mpeg', '.doc', '.txt']

if not os.path.exists(local_folder):
    os.makedirs(local_folder)

s3 = boto3.client('s3')

def is_valid_file(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower() in allowed_extensions

def backup_files():
    logging.info("Backup started.")

    for file in os.listdir(local_folder):
        local_path = os.path.join(local_folder, file)
        if os.path.isfile(local_path) and is_valid_file(file):
            try:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                s3_key = f"{backup_folder}{timestamp}_{file}"
                s3.upload_file(Filename=local_path, Bucket=bucket_name, Key=s3_key)
                logging.info(f"Backed up '{file}' to '{s3_key}'.")
                print(f"Uploaded '{file}' as '{s3_key}'")
            except Exception as e:
                logging.error(f"Failed to upload '{file}': {e}")
                print(f"Failed to upload '{file}': {e}")
    logging.info("Backup complete.")

if __name__ == "__main__":
    while True:
        backup_files()
        print("Waiting for 60 seconds before next backup...\n")
        time.sleep(60)
