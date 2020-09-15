import sys
import boto3
import datetime

BUCKET = 'zkloud.zealbots.com'
AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''

def FetchBucktes(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY):
    s3client = boto3.client(
     's3',
     aws_access_key_id=AWS_ACCESS_KEY_ID,
     aws_secret_access_key=AWS_SECRET_ACCESS_KEY
     #aws_session_token='if token',
     )
    allbuckets = s3client.list_buckets()
    for bucket in allbuckets['Buckets']:
        print(bucket)



def separateBucketSize(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,BUCKET):
    s3 = boto3.resource('s3',
      aws_access_key_id=AWS_ACCESS_KEY_ID,
      aws_secret_access_key=AWS_SECRET_ACCESS_KEY
      #aws_session_token='if token',
     )
    size_byte=0
    MB = 1024*1024
    my_bucket=s3.Bucket(BUCKET)
    for my_bucket_object in my_bucket.objects.all():
        if my_bucket_object.key.startswith("zkloud/Zcusr11111/"):
            print(my_bucket_object.key)
            size_byte=size_byte+my_bucket_object.size
    totalsize_gb=size_byte/1000/1024/1024
    print(size_byte)
    print(size_byte/MB)
    print(totalsize_gb)

if __name__ == "__main__":
    FetchBucktes(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
    separateBucketSize(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,BUCKET)
