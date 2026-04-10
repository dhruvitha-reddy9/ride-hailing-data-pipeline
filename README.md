#  Ride-Hailing Data Pipeline (GCP | PySpark | BigQuery | Airflow)



# Project Overview

This project implements an **end-to-end batch data pipeline** simulating a real-world ride-hailing platform (similar to Uber/Ola).

The pipeline ingests data from an external API, processes it using distributed computing (PySpark), and loads it into a data warehouse (BigQuery) for analytics.


# Objective

* Build a scalable **data lake → processing → warehouse pipeline**
* Handle real-world challenges like:

  * Schema mismatches
  * Data type inconsistencies
  * Cloud resource limitations
* Enable **analytical querying** on processed data


# Architecture

```
External API
     ↓
Python Ingestion Script (Local)
     ↓
Google Cloud Storage (Data Lake - Raw)
     ↓
Dataproc (PySpark Processing)
     ↓
Google Cloud Storage (Processed - Parquet)
     ↓
BigQuery (Data Warehouse)
     ↓
Analytics / BI
```


# Tech Stack

| Layer           | Technology               |
| --------------- | ------------------------ |
| Ingestion       | Python, Requests, Pandas |
| Storage         | Google Cloud Storage     |
| Processing      | PySpark (Dataproc)       |
| Orchestration   | Airflow (Cloud Composer) |
| Data Warehouse  | BigQuery                 |
| Version Control | Git & GitHub             |


# Project Structure

```
ride-hailing-pipeline/
│
├── ingestion/              # API ingestion scripts
├── spark_jobs/             # PySpark transformation logic
├── schemas/                # Raw data schemas
├── bq_schema/              # BigQuery table definitions
├── airflow/                # DAG for orchestration
├── scripts/                # Setup automation scripts
│
├── requirements.txt
├── .gitignore
└── README.md
```

# Pipeline Workflow

## 1️ Data Ingestion

* Fetch data from external API
* Convert to structured format using Pandas
* Upload to GCS (raw layer)

## 2️ Data Processing (PySpark)

* Read raw data from GCS
* Apply transformations:

  * Data type casting
  * Timestamp handling
  * Derived columns
* Store output in **Parquet format**

## 3️ Data Warehouse (BigQuery)

* Load processed data into BigQuery
* Apply structured schema
* Enable fast analytical queries

## 4️ Orchestration (Airflow)

* Automate pipeline steps:

  ```
  ingest → transform → load → validate
  ```


# Data Model

## Fact Table

* `fact_trips`

  * Stores transactional data

## Dimension Tables

* `dim_user`
* `dim_location`

 Designed using **Star Schema** for efficient analytics


# Sample Queries

```sql
-- Total records
SELECT COUNT(*) FROM ride_dw.fact_trips;

-- Top users by activity
SELECT userId, COUNT(*) as total
FROM ride_dw.fact_trips
GROUP BY userId
ORDER BY total DESC;

-- Daily ingestion trend
SELECT DATE(processed_time), COUNT(*)
FROM ride_dw.fact_trips
GROUP BY 1;
```

# How to Run

## 1. Setup GCP Resources

```bash
bash scripts/setup.sh YOUR_PROJECT_ID
```

## 2. Run Ingestion

```bash
python ingestion/fetch_api_data.py
```

## 3. Run Spark Job

```bash
gcloud dataproc jobs submit pyspark spark_jobs/transform.py
```

## 4. Load to BigQuery

```bash
bq load --source_format=PARQUET ride_dw.fact_trips gs://.../processed/*
```

# Challenges & Solutions

## Schema Mismatch

* Issue: BigQuery rejected new fields
* Solution: Aligned schema with source data

## Data Type Issues

* Issue: Timestamp stored as string
* Solution: Cast using PySpark (`to_timestamp`)

## GCP Quota Limits

* Issue: Cluster creation failed
* Solution: Used single-node cluster

## Zone Availability

* Issue: Resource unavailable in zone
* Solution: Switched zones / auto selection


# Key Learnings

* Data Lake vs Data Warehouse architecture
* Distributed processing using Spark
* Schema enforcement and evolution
* Cloud resource management
* End-to-end pipeline design


# Interview Explanation (Short)

> Built an end-to-end batch data pipeline using PySpark on Dataproc, ingesting API data into GCS, transforming it into Parquet format, and loading into BigQuery for analytics, with Airflow-based orchestration.


# Future Improvements

* Add real-time streaming (Kafka / PubSub)
* Implement incremental loading
* Add monitoring & alerting
* CI/CD pipeline for automation


# Author

**Dhruvitha Reddy**

