import tweepy, json, os
import pandas as pd
from google.cloud import storage
import yfinance as yf
from datetime import datetime

msft = yf.Ticker('MSFT')

today = datetime.today().strftime('%d_%m_%Y_%H_%M')

# get historical market data
hist = msft.history(period="1d", interval="1h")

hist.to_csv(f'yahoo_{today}.csv')