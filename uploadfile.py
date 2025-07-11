import boto3

s3 = boto3.client('s3')
bucket_name = '24030142004'
filename = "cloud.txt"

try:
    s3.upload_file(Filename=filename, Bucket=bucket_name, Key=filename)
    print(f"Uploaded '{filename}' to bucket '{bucket_name}'.")
except Exception as e:
    print(f"Error uploading file: {e}")