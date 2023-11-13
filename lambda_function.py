import boto3
from PIL import Image
import imagehash
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Example input event
    # {
    #     "approved_bucket": "approved-vehicle-images",
    #     "pending_bucket": "pending-vehicle-images",
    #     "image_key_approved": "image1.jpg",
    #     "image_key_pending": "image2.jpg"
    # }

    # Extract input parameters from the event
    approved_bucket = event.get("approved_bucket")
    pending_bucket = event.get("pending_bucket")
    image_key_approved = event.get("image_key_approved")
    image_key_pending = event.get("image_key_pending")

    # Download images from S3
    approved_image = download_image(approved_bucket, image_key_approved)
    pending_image = download_image(pending_bucket, image_key_pending)

    # Calculate perceptual hash for both images
    hash_approved = imagehash.average_hash(approved_image)
    hash_pending = imagehash.average_hash(pending_image)

    # Compare hashes to check if images are the same
    are_images_same = hash_approved == hash_pending

    response = {
        "are_images_same": are_images_same
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }

def download_image(bucket, key):
    obj = s3.get_object(Bucket=bucket, Key=key)
    image_data = obj['Body'].read()
    return Image.open(io.BytesIO(image_data))

