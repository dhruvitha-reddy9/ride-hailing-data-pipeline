from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Default arguments
default_args = {
    "owner": "data-engineer",
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

# Define DAG
with DAG(
    dag_id="ride_hailing_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
) as dag:

    # Step 1: Ingestion (simulate API call)
    ingest_data = BashOperator(
        task_id="ingest_data",
        bash_command="echo 'Ingesting data from API'"
    )

    # Step 2: Spark transformation (Dataproc job)
    spark_transform = BashOperator(
        task_id="spark_transform",
        bash_command="""
        gcloud dataproc jobs submit pyspark \
        gs://ride-data-lake-123/scripts/transform.py \
        --cluster=ride-cluster \
        --region=asia-south1
        """
    )

    # Step 3: Load to BigQuery
    load_to_bq = BashOperator(
        task_id="load_to_bigquery",
        bash_command="""
        bq load --source_format=PARQUET \
        ride_dw.fact_trips \
        gs://ride-data-lake-123/processed/trips/*
        """
    )

    # Step 4: Data validation
    validate_data = BashOperator(
        task_id="validate_data",
        bash_command="""
        bq query --use_legacy_sql=false \
        'SELECT COUNT(*) FROM ride_dw.fact_trips'
        """
    )

    # DAG flow
    ingest_data >> spark_transform >> load_to_bq >> validate_data