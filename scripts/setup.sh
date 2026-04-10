#!/bin/bash

# Exit if any command fails
set -e

PROJECT_ID=$1
REGION="asia-south1"
BUCKET_NAME="ride-data-lake-$PROJECT_ID"

echo "Setting project..."
gcloud config set project $PROJECT_ID

echo "Enabling required services..."
gcloud services enable \
    storage.googleapis.com \
    dataproc.googleapis.com \
    bigquery.googleapis.com

echo "Creating GCS bucket..."
gsutil mb -l $REGION gs://$BUCKET_NAME || echo "Bucket already exists"

echo "Creating BigQuery dataset..."
bq mk ride_dw || echo "Dataset already exists"

echo "Setup complete!"