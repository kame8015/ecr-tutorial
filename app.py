import json
import os

import nltk

nltk.data.path.append(os.environ["LAMBDA_TASK_ROOT"])

def handler(event, context):
    tokens = nltk.word_tokenize(event["sentence"])

    return {
        "statusCode": 200,
        "body": json.dumps({"tokens": tokens})
    }

