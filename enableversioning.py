import boto3

bucket_name = '24030142004'
s3 = boto3.client('s3')
try:
    s3.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={'Status': 'Enabled'}
    )
    print(f"Versioning enabled for bucket: {bucket_name}")
except Exception as e:
    print(f"Error enabling versioning: {e}")
