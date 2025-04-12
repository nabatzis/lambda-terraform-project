variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
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