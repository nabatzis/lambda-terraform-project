variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "s3_bucket_name" {
  description = "Name of the S3 bucket that triggers the Lambda function"
  type        = string
  default     = "my-lambda-trigger-bucket"
}

variable "s3_filter_prefix" {
  description = "Optional prefix filter for S3 events (e.g., 'uploads/')"
  type        = string
  default     = ""
}

variable "s3_filter_suffix" {
  description = "Optional suffix filter for S3 events (e.g., '.jpg')"
  type        = string
  default     = ""
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
  default     = "terraform-python-lambda"
}

variable "lambda_timeout" {
  description = "Lambda function timeout (in seconds)"
  type        = number
  default     = 10
}

variable "lambda_memory_size" {
  description = "Lambda function memory size (in MB)"
  type        = number
  default     = 128
}

variable "environment_variables" {
  description = "Environment variables for the Lambda function"
  type        = map(string)
  default     = {
    ENVIRONMENT = "dev"
  }
}