from google.cloud import storage
import yfinance as yf
from datetime import datetime

bucket_name='yahoo_stock_airflow_bucket'

def extract_data_from_yahoo(stock_name: str='MSFT'):
    msft = yf.Ticker(stock_name)

    today = datetime.today().strftime('%d_%m_%Y_%H_%M')

    # get historical market data
    hist = msft.history(period="1d", interval="1h")

    hist.to_csv(f'gs://yahoo_stock_airflow_bucket/yahoo_{stock_name}_{today}.csv')

# QDrbywkxdhhZmeHa



    # """Write and read a blob from GCS using file-like IO"""
    # # The ID of your GCS bucket
    # # bucket_name = "your-bucket-name"

    # # The ID of your new GCS object
    # # blob_name = "storage-object-name"

    # storage_client = storage.Client()
    # bucket = storage_client.bucket(bucket_name)
    # blob = bucket.blob(blob_name)

    # # Mode can be specified as wb/rb for bytes mode.
    # # See: https://docs.python.org/3/library/io.html
    # with blob.open("w") as f:
    #     f.write("Hello world")

    # with blob.open("r") as f:
    #     print(f.read())
