import json
import os

import nltk

nltk.data.path.append(os.environ["LAMBDA_TASK_ROOT"])

def handler(event, context):
    print(event)
    event_body = json.loads(event["body"])
    print(event_body)
    tokens = nltk.word_tokenize(event_body["sentence"])


    return {
        "statusCode": 200,
        "body": json.dumps({"tokens": tokens})
    }

