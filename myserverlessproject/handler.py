# handler.py
import json

def hello(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello, World!',
            'input': event,
        }),
    }
