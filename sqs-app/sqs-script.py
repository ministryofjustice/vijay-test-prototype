import json
import boto3
import os
import time
num = 1
while (num <= 2):
    try:
      sqs = boto3.client('sqs', region_name='eu-west-2', aws_access_key_id=os.getenv('ACCESS_KEY'),aws_secret_access_key=os.getenv('SECRET_KEY'))
      response = sqs.send_message(QueueUrl=os.getenv('QUEUE_URL'),MessageBody="Hello CP")
      print(response)
      num = num + 1
    except Exception as error:
      print (error)
print("Sleep time")
time.sleep(os.getenv('SLEEP_TIME'))