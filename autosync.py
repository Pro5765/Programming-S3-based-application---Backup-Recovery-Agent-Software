import boto3
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

bucket_name = '24030142004'
local_folder = 'sync_folder/'
allowed_extensions = ['.pdf', '.jpeg', '.jpg', '.mpeg', '.doc', '.txt']
os.makedirs(local_folder, exist_ok=True)
logging.basicConfig(
    filename='file_sync.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

s3 = boto3.client('s3')

def is_valid_file(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower() in allowed_extensions

def upload_file_to_s3(filepath):
    filename = os.path.basename(filepath)
    if not is_valid_file(filename):
        logging.info(f"Skipped (not valid type): {filename}")
        return
    try:
        s3.upload_file(Filename=filepath, Bucket=bucket_name, Key=f'synced/{filename}')
        logging.info(f"Uploaded: {filename}")
        print(f"Synced: {filename}")
    except Exception as e:
        logging.error(f"Failed to upload '{filename}': {e}")
        print(f"Upload error: {e}")

def delete_file_from_s3(filename):
    try:
        s3.delete_object(Bucket=bucket_name, Key=f'synced/{filename}')
        logging.info(f"Deleted from S3: {filename}")
        print(f"Deleted from S3: {filename}")
    except Exception as e:
        logging.error(f"Failed to delete '{filename}': {e}")
        print(f"Deletion error: {e}")

class S3SyncHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            upload_file_to_s3(event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            upload_file_to_s3(event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            delete_file_from_s3(filename)

def start_watching():
    print("Watching for changes...")
    event_handler = S3SyncHandler()
    observer = Observer()
    observer.schedule(event_handler, path=local_folder, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
if __name__ == "__main__":
    start_watching()
