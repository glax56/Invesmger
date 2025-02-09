import yfinance as yf
import pandas as pd

# Define tickers and date range
tickers = ["AAPL", "MSFT", "GOOGL", "TSLA", "SPY", "BND"]
start_date = "2015-01-01"
end_date = "2025-01-01"

# Fetch data using yfinance
print("Fetching stock data...")
try:
    stock_data = yf.download(tickers, start=start_date, end=end_date)
    
    # Print the full response structure
    print("Raw Data Columns:", stock_data.columns)

    # Check if "Adj Close" exists
    if "Adj Close" in stock_data:
        stock_data = stock_data["Adj Close"]
        print("Data fetched successfully!")
    else:
        print("Warning: 'Adj Close' column not found. Displaying full data structure instead.")
    
except Exception as e:
    print(f"Error fetching data: {e}")
    stock_data = None

# Display first few rows
if stock_data is not None:
    display(stock_data.head())  # Use display() for Jupyter Notebook
else:
    print("No stock data fetched.")