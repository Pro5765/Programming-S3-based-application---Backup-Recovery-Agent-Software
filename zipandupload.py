import boto3
import os
import zipfile
from datetime import datetime

bucket_name = '24030142004'
source_folder = 'zip_source/'
zip_filename = 'backup.zip'

os.makedirs(source_folder, exist_ok=True)

s3 = boto3.client('s3')
response = s3.list_object_versions(Bucket='24030142004', Prefix='zips/backup.zip')

for version in response.get('Versions', []):
    print(f"VersionId: {version['VersionId']} | LastModified: {version['LastModified']}")


def create_zip():
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_folder)
                zipf.write(file_path, arcname)
    print(f"Created ZIP: {zip_filename}")

def upload_zip():
    s3 = boto3.client('s3')
    try:
        s3.upload_file(zip_filename, bucket_name, f'zips/{zip_filename}')
        print(f"Uploaded ZIP to S3 bucket '{bucket_name}' with versioning.")
    except Exception as e:
        print(f"Failed to upload ZIP: {e}")

if __name__ == "__main__":
    create_zip()
    upload_zip()
