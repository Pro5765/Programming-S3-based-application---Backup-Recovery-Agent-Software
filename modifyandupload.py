import boto3

bucket_name = '24030142004'
filename = "cloud.txt"

try:
    with open(filename, 'a') as f:
        f.write("\nThis is additional content.")
    print(f"Modified local file '{filename}'.")
    s3 = boto3.client('s3')
    s3.upload_file(Filename=filename, Bucket=bucket_name, Key=filename)
    print(f"Re-uploaded modified file '{filename}' to bucket '{bucket_name}'.")

except Exception as e:
    print(f"Error modifying/uploading file: {e}")
