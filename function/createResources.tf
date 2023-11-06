provider "aws" {
  region = "eu-north-1"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "sort-student-bucket"
  acl    = "public"
}

resource "aws_lambda_function" "my_lambda" {
  function_name = "generateClasses"
  handler       = "index.html"
  runtime       = "Python 3.9"

  # ... altre opzioni specifiche per la tua Lambda function
}
