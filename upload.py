import boto3

s3 = boto3.client("s3")

bucket_name = "jennifer-bucket-2025"
local_file = "image.jpg"
s3_file = "images/image.jpg"

s3.upload_file(
    local_file,
    bucket_name,
    s3_file,
    ExtraArgs={"ContentType": "image/jpeg"}
)

print("Upload successful!")