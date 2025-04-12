output "lambda_function_arn" {
  description = "ARN of the Lambda function"
  value       = aws_lambda_function.function.arn
}

output "lambda_function_name" {
  description = "Name of the Lambda function"
  value       = aws_lambda_function.function.function_name
}

output "lambda_invoke_url" {
  description = "Invoke URL for the Lambda function (if API Gateway was configured)"
  value       = "Use AWS CLI: aws lambda invoke --function-name ${aws_lambda_function.function.function_name} --payload '{}' response.json"
}