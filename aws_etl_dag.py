from airflow import DAG
from airflow.providers.amazon.aws.operators.glue import AwsGlueJobOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
}

with DAG(
    dag_id="aws_data_pipeline",
    default_args=default_args,
    description="AWS ETL pipeline using Glue & Airflow",
    schedule_interval="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["aws", "data-engineering"],
) as dag:

    glue_job = AwsGlueJobOperator(
        task_id="run_glue_job",
        job_name="aws_glue_etl_job",
        script_location="s3://rahul-aws-data-raw-bucket/glue_etl_job.py",
        region_name="us-east-1",
    )

    glue_job
