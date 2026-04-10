import requests
import pandas as pd
from datetime import datetime

# 🔹 Replace with real API (for now using mock structure)
API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_data():
    response = requests.get(API_URL)

    if response.status_code != 200:
        raise Exception(f"API failed with status {response.status_code}")

    return response.json()


def transform_to_dataframe(data):
    df = pd.DataFrame(data)

    # Add ingestion timestamp
    df["ingestion_time"] = datetime.now()

    return df


def save_file(df):
    filename = f"trips_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(filename, index=False)

    print(f"Saved file: {filename}")
    return filename


if __name__ == "__main__":
    data = fetch_data()
    df = transform_to_dataframe(data)
    file = save_file(df)