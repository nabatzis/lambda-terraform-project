# 1. Using AWS ECS (Elastic Container Service)

This is the most common method to run Docker containers from Lambda:

```python
import boto3
import json

def lambda_handler(event, context):
    # Initialize ECS client
    ecs_client = boto3.client('ecs')ß

    # Run the task
    response = ecs_client.run_task(
        cluster='your-ecs-cluster',
        taskDefinition='your-task-definition:1',  # Include version number
        launchType='FARGATE',  # Or 'EC2' if using EC2 launch type
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': ['subnet-12345', 'subnet-67890'],
                'securityGroups': ['sg-12345'],
                'assignPublicIp': 'ENABLED'  # Or 'DISABLED' for private subnets
            }
        },
        overrides={
            'containerOverrides': [
                {
                    'name': 'your-container-name',
                    'environment': [
                        {
                            'name': 'PARAMETER_1',
                            'value': 'value1'
                        }
                    ]
                }
            ]
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Task started successfully!')
    }
```

# 2. Using AWS Batch

AWS Batch is ideal for batch computing workloads:

```python
import boto3
import json

def lambda_handler(event, context):
    # Initialize Batch client
    batch_client = boto3.client('batch')

    # Submit a job
    response = batch_client.submit_job(
        jobName='job-triggered-by-lambda',
        jobQueue='your-job-queue',
        jobDefinition='your-job-definition',
        parameters={
            'param1': 'value1',
            'param2': 'value2'
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps(f"Job submitted with ID: {response['jobId']}")
    }

```

# 3. Using AWS Lambda Container Images

You can also package your Lambda function as a container, though this doesn't "trigger" a separate container:

```terraform
resource "aws_lambda_function" "docker_lambda" {
  function_name = "docker-lambda-function"
  role          = aws_iam_role.lambda_role.arn
  package_type  = "Image"
  image_uri     = "${aws_ecr_repository.lambda_repo.repository_url}:latest"
  timeout       = 30
  memory_size   = 512
}
```
