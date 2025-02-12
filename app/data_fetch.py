import yfinance as yf
import pandas as pd
import os

def fetch_stock_data(tickers, start_date="2015-01-01", end_date="2025-01-01", save_csv=True):
    """
    Fetch historical close prices for given stock tickers.
    """
    print(f"Fetching stock data for: {tickers}")
    try:
        stock_data = yf.download(tickers, start=start_date, end=end_date)
        
        if "Close" in stock_data:
            stock_data = stock_data["Close"]
            print("Data fetched successfully!")
        else:
            print("Warning: 'Close' column not found.")
        
        if save_csv:
            os.makedirs("data", exist_ok=True)
            stock_data.to_csv("data/stock_data.csv")
            print("Data saved to data/stock_data.csv")

        return stock_data

    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None
