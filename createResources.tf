provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-unique-bucket-name"
  acl    = "private"
}

resource "aws_lambda_function" "my_lambda" {
  function_name = "my-lambda-function"
  handler       = "index.handler"
  runtime       = "nodejs14.x"

  # ... altre opzioni specifiche per la tua Lambda function
}

resource "aws_api_gateway_rest_api" "my_api" {
  name        = "my-api"
  description = "My API"

  # ... altre opzioni specifiche per il tuo API Gateway
}
