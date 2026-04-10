# Ride-Hailing Data Pipeline (GCP | PySpark | BigQuery)

---

## Overview

This project implements an end-to-end batch data pipeline that ingests data from an external API, processes it using PySpark, and loads it into BigQuery for analytics.

---

## Architecture

```
API → GCS (Raw) → Dataproc (Spark) → GCS (Processed) → BigQuery → Analytics
```

---

## Tech Stack

* Python (Requests, Pandas)
* PySpark (Dataproc)
* Google Cloud Storage (Data Lake)
* BigQuery (Data Warehouse)
* Airflow (Orchestration - DAG design)
* Git & GitHub

---

## Pipeline Flow

### 1. Ingestion

* Fetch data from external API
* Convert to structured format
* Store raw data in Google Cloud Storage

### 2. Processing

* Read raw data using PySpark
* Perform transformations and type casting
* Handle timestamp conversions
* Store output in Parquet format

### 3. Data Warehouse

* Load processed data into BigQuery
* Apply structured schema
* Enable analytical queries

### 4. Orchestration

* Designed Airflow DAG for pipeline automation:

  ```
  ingest → transform → load → validate
  ```

---

## Data Model

* `fact_trips` – main transactional table
* `dim_user` – derived dimension table

---

## Key Highlights

* Built scalable cloud-based data pipeline
* Implemented schema handling and data type corrections
* Optimized storage using Parquet format
* Designed Airflow DAG for orchestration
* Automated infrastructure setup using shell script

---

## Learnings

* Data Lake vs Data Warehouse architecture
* Distributed data processing using Spark
* Handling schema mismatches and data types
* Working with GCP services and resource constraints
* End-to-end pipeline design

---

## How to Run

```bash
# Setup infrastructure
bash scripts/setup.sh YOUR_PROJECT_ID

# Run ingestion
python ingestion/fetch_api_data.py

# Run Spark job
gcloud dataproc jobs submit pyspark spark_jobs/transform.py
```

---

## Summary

Built an end-to-end data pipeline using PySpark on Dataproc, ingesting API data into GCS, transforming it into Parquet format, and loading it into BigQuery, with Airflow-based orchestration design.

---

## Author

Dhruvitha Reddy
