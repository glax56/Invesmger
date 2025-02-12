import numpy as np
import pandas as pd

def calculate_volatility(stock_data):
    """
    Calculate annualized volatility for each stock.
    """
    daily_returns = stock_data.pct_change().dropna()
    return daily_returns.std() * np.sqrt(252)

def calculate_sharpe_ratio(stock_data, risk_free_rate=0.02):
    """
    Calculate Sharpe Ratio for each stock.
    """
    daily_returns = stock_data.pct_change().dropna()
    excess_returns = daily_returns.mean() * 252 - risk_free_rate
    volatility = daily_returns.std() * np.sqrt(252)
    return excess_returns / volatility

def calculate_max_drawdown(stock_data):
    """
    Calculate the maximum drawdown for each stock.
    """
    cumulative_returns = (1 + stock_data.pct_change()).cumprod()
    rolling_max = cumulative_returns.cummax()
    drawdown = (cumulative_returns - rolling_max) / rolling_max
    return drawdown.min()

def evaluate_portfolio_risk(stock_data):
    """
    Evaluate the risk of the portfolio using various metrics.
    """
    risk_metrics = pd.DataFrame(index=stock_data.columns)
    
    risk_metrics["Volatility"] = calculate_volatility(stock_data)
    risk_metrics["Sharpe Ratio"] = calculate_sharpe_ratio(stock_data)
    risk_metrics["Max Drawdown"] = calculate_max_drawdown(stock_data)
    
    return risk_metrics

def suggest_portfolio_adjustments(risk_metrics, risk_level):
    """
    Suggest portfolio adjustments based on the user's risk level.
    """
    adjustments = {}
    
    if risk_level == "low":
        high_risk_assets = risk_metrics[risk_metrics["Volatility"] > 0.25].index.tolist()
        for asset in high_risk_assets:
            adjustments[asset] = "Consider reducing exposure or shifting to lower-risk assets."
    elif risk_level == "medium":
        balanced_assets = risk_metrics[risk_metrics["Sharpe Ratio"] > 0.5].index.tolist()
        for asset in balanced_assets:
            adjustments[asset] = "Portfolio is well-balanced, consider minor optimizations."
    elif risk_level == "high":
        low_risk_assets = risk_metrics[risk_metrics["Volatility"] < 0.15].index.tolist()
        for asset in low_risk_assets:
            adjustments[asset] = "Consider increasing exposure to higher-growth assets."
    
    return adjustments

if __name__ == "__main__":
    from app.data_fetch import fetch_stock_data
    from app.portfolio_creation import create_portfolio
    
    tickers = ["AAPL", "MSFT", "GOOGL", "TSLA", "SPY"]
    stock_data = fetch_stock_data(tickers, start_date="2024-01-01")
    
    risk_metrics = evaluate_portfolio_risk(stock_data)
    print("Portfolio Risk Metrics:")
    print(risk_metrics)
    
    risk_level = "medium"  # Change based on user input
    adjustments = suggest_portfolio_adjustments(risk_metrics, risk_level)
    print("Suggested Portfolio Adjustments:")
    print(adjustments)