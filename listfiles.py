import boto3

s3 = boto3.client('s3')
bucket_name = '24030142004'

try:
    response = s3.list_objects_v2(Bucket=bucket_name)
    print("Files in bucket:")
    for obj in response.get('Contents', []):
        print("-", obj['Key'])

except Exception as e:
    print(f"Error listing filesL {e}")