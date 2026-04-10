CREATE TABLE ride_dw.fact_trips (
    userId STRING,
    id STRING,
    title STRING,
    body STRING,
    ingestion_time TIMESTAMP,
    processed_time TIMESTAMP
)
PARTITION BY DATE(processed_time);