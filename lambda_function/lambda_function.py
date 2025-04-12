import boto3
import json
import logging
import urllib

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    """
    Main Lambda function handler trigerred by S3 events
    
    Parameters:
        event (dict): S3 Event data from the trigger
        context (LambdaContext): Runtime information
        
    Returns:
        dict: Response object
    """
    logger.info('Received event: %s', json.dumps(event))
    
    # Get the S3 bucket and object details from the event
    try:
        # Get bucket name and object key from event
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
        
        logger.info(f"Processing file: s3://{bucket}/{key}")
        
        # Get the object from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        
        # Process the file
        # (Example: read the content if it's a text file)
        if key.endswith('.txt'):
            content = response['Body'].read().decode('utf-8')
            logger.info(f"File content (first 100 chars): {content[:100]}")
        else:
            file_size = response['ContentLength']
            logger.info(f"File size: {file_size} bytes")

        # Your processing logic here
    
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': f"Successfully processed file: {key}",
                'event': event
            })
        }
    except Exception as e:
        logger.error(f"Error processing S3 event: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f"Error processing file: {str(e)}"
            })
        }