import json

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
        logged['logged'] = data['log']
        
        return {
            'statusCode': 200,
            'body': json.dumps(logged)
        }
    except Exception as e:
        logged['logged'] = 'Failed'
        return {
            'statusCode': 400,
            'body': json.dumps(logged)
        }
