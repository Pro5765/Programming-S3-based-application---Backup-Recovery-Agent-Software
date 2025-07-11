import boto3
import os
import logging

logging.basicConfig(
    filename='s3_upload.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
bucket_name = '24030142004'
filename = 'cloud.pdf'
allowed_extensions = ['.pdf', '.jpeg', '.jpg', '.mpeg', '.doc', '.txt']
def is_valid_file(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower() in allowed_extensions
def upload_file():
    s3 = boto3.client('s3')
    if not os.path.exists(filename):
        logging.error(f"File '{filename}' does not exist.")
        print("File not found.")
        return
    if not is_valid_file(filename):
        logging.warning(f"Invalid file type: {filename}")
        print("Invalid file type. Only PDF, JPEG, MPEG, DOC, TXT are allowed.")
        return
    try:
        s3.upload_file(Filename=filename, Bucket=bucket_name, Key=filename)
        logging.info(f"Successfully uploaded '{filename}' to bucket '{bucket_name}'.")
        print(f"Uploaded '{filename}' successfully.")
    except Exception as e:
        logging.error(f"Error uploading file '{filename}': {e}")
        print(f"Upload failed: {e}")
if __name__ == "__main__":
    upload_file()
