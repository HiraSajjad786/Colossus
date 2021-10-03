import os
import logging
import boto3
from environs import Env
from botocore.exceptions import ClientError
import hybrid

env = Env()
env.read_env()

AWS_S3_CREDS = {
    "aws_access_key_id": os.getenv("ACCESS_KEY_ID"),
    "aws_secret_access_key":os.getenv("SECRET_ACCESS_KEY")
}

bucket = os.getenv("BUCKET_NAME")
# upload
def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3', **AWS_S3_CREDS)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        print("something is wrong here")
        logging.error(e)
        return False
    return True


# menu
print("Welcome to Sefy")
print("# Press 1 to upload file")
print("# Press 2 to download file")
print("# other key to exit")
op = int(input())
if (op == 1):
    file_location = input("Enter file name with path: (with \\) ")
    obj = input("Enter the object name: ")
    try:
        hybrid.main(file_location)
        upload_file(file_location, bucket, obj)
        print("DONE!")
    except Exception as e:
        raise e
elif (op == 2):
    obj1 = input("Enter Object name: ")
    s3 = boto3.client('s3', **AWS_S3_CREDS)
    s3.download_file(bucket, obj1, obj1)
else:
    os._exit(0)
