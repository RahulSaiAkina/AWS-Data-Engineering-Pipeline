terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "raw_bucket" {
  bucket = "rahul-aws-data-raw-bucket"
}

resource "aws_s3_bucket" "curated_bucket" {
  bucket = "rahul-aws-data-curated-bucket"
}
