import yfinance as yf
import pandas as pd
import numpy as np

def get_top_performers(asset_class, num_tickers=3):
    """
    Fetch the top-performing tickers for a given asset class over the past 3 months using 'Close' prices only.
    """
    asset_class_mapping = {
        "ETF": ["SPY", "QQQ", "VTI", "VOO"],
        "Bonds": ["BND", "AGG", "TLT"],
        "Tech": ["AAPL", "MSFT", "GOOGL", "TSLA"],
        "Energy": ["XOM", "CVX", "VLO"]
    }
    
    tickers = asset_class_mapping.get(asset_class, [])
    if not tickers:
        return []
    
    data = yf.download(tickers, period="3mo", interval="1d")
    
    if "Close" in data.columns:
        price_data = data["Close"]
    else:
        print(f"Error: No valid 'Close' price data for {asset_class}.")
        return []
    
    returns = price_data.pct_change().sum().sort_values(ascending=False)
    
    return list(returns.index[:num_tickers])

def create_portfolio(user_defined=None, risk_level="medium"):
    """
    Create a portfolio based on user input or generate one based on risk-based asset allocations.
    """
    allocation = {
        "low": {"ETF": 0.50, "Bonds": 0.40, "Tech": 0.05, "Energy": 0.05},
        "medium": {"ETF": 0.40, "Bonds": 0.25, "Tech": 0.25, "Energy": 0.10},
        "high": {"ETF": 0.20, "Bonds": 0.10, "Tech": 0.50, "Energy": 0.20}
    }[risk_level]

    portfolio = {}
    for asset_class, percentage in allocation.items():
        top_tickers = get_top_performers(asset_class, num_tickers=2)
        for ticker in top_tickers:
            portfolio[ticker] = percentage / len(top_tickers)  

    return portfolio