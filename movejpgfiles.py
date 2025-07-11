import boto3
import os

bucket_name = '24030142004'
s3 = boto3.client('s3')

try:
    response = s3.list_objects_v2(Bucket=bucket_name)
    contents = response.get('Contents', [])
    for obj in contents:
        key = obj['Key']
        if key.endswith('.jpg') or key.endswith('.jpeg'):
            new_key = f'pictures/{os.path.basename(key)}'
            s3.copy_object(
                CopySource={'Bucket': bucket_name, 'Key': key},
                Bucket=bucket_name,
                Key=new_key
            )

            s3.delete_object(Bucket=bucket_name, Key=key)
            print(f"Moved '{key}' to '{new_key}'")
    if not contents:
        print("Bucket is empty or contains no .jpg files.")
except Exception as e:
    print(f"Error while moving files: {e}")