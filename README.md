# AWS Data Engineering Project 🚀

This project demonstrates an end-to-end AWS Data Engineering pipeline.

## Components
- **Terraform** → Provisions AWS resources (S3, Glue, IAM)
- **Glue Jobs** → Runs ETL to transform raw data into curated format
- **Airflow DAG** → Orchestrates data pipeline execution
- **GitHub Actions** → CI/CD for Terraform deployments

## Workflow
1. Raw data is uploaded to **S3**
2. Glue job processes & loads curated data into **S3 Silver layer**
3. Airflow DAG schedules & monitors pipeline
4. GitHub Actions automates infrastructure deployment

---
Clone and showcase this repo to highlight your AWS Data Engineering skills!
