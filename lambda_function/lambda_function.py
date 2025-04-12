import json
import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Main Lambda function handler
    
    Parameters:
        event (dict): Event data from the trigger
        context (LambdaContext): Runtime information
        
    Returns:
        dict: Response object
    """
    logger.info('Received event: %s', json.dumps(event))
    
    # Your business logic here
    message = "Hello from Lambda created with Terraform!"
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'message': message,
            'event': event
        })
    }