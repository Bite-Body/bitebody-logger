import json
import boto3
from datetime import datetime

# Get the service resource
dynamodb = boto3.resource('dynamodb')

def insert_data(log):
    now = datetime.now()
    log_name = 'LOG-' + str(now)
    table = dynamodb.Table('Logs')
    table.put_item(
        Item={
            'Log_Name': log_name,
            'Log_Message': log
        }
    )

def lambda_handler(event, context):
    # Need to make sure it saves data to Dynamo
    # POST the following in body as JSON:
    '''
    {
	"log": {
		"source": "Bitebody.xyz API",
		"date": "2020-02-19T05:02:57+0000",
		"action": "/user/all",
		"ip-address": "192.168.0.1"
    	}
    }
    '''
    
    logged = {}
    
    try:
        data = json.loads(event['body'])
        insert_data(data['log'])
        logged['logged'] = data['log']
        
        return {
            'statusCode': 200,
            'body': json.dumps(logged)
        }
    except Exception as e:
        logged['error'] = str(e)
        return {
            'statusCode': 400,
            'body': json.dumps(logged)
        }
