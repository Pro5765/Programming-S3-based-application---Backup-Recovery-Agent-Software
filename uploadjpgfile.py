import boto3

bucket_name = '24030142004'
file_path = 'cloud.jpg'

s3 = boto3.client('s3')

try:
    s3.upload_file(Filename=file_path, Bucket=bucket_name, Key='image.jpg')
    print(f"Uploaded '{file_path}' to bucket '{bucket_name}'.")
except Exception as e:
    print(f"Error uploading .jpg file: {e}")
