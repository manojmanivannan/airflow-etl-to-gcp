from google.cloud import storage
import yfinance as yf
from datetime import datetime

bucket_name='yahoo_stock_airflow_bucket'

def extract_data_from_yahoo(stock_name: str='MSFT'):
    
    msft = yf.Ticker(stock_name)

    today = datetime.today().strftime('%d_%m_%Y_%H_%M')

    # get historical market data
    hist = msft.history(period="1d", interval="1h")

    hist.to_csv(f'gs://{bucket_name}/yahoo_{stock_name}_{today}.csv')
