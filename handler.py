import random
import json

import boto3

def random_sandwich(event, context):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket='sandwichme.bubblehouse.org')
    item = random.choice(response['Contents'])

    url = "https://s3.amazonaws.com/sandwichme.bubblehouse.org/%s" % (item['Key'])
    
    body = {
        "sandwich": url
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

