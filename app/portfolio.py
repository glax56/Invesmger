import pandas as pd

def get_portfolio_allocation(risk_level, tickers):
    """
    Generate a portfolio allocation based on the given risk level.

    Parameters:
        risk_level (str): "low", "medium", or "high".
        tickers (list): List of available stock tickers.

    Returns:
        dict: Asset allocation weights.
    """

    # Default allocation structure
    allocations = {
        "low": {
            "BND": 0.50,  # Bonds
            "SPY": 0.30,  # S&P 500 Index
            "AAPL": 0.10,  # Stable Blue-chip
            "GOOGL": 0.10  # Tech Exposure
        },
        "medium": {
            "SPY": 0.40,  # S&P 500 Index
            "AAPL": 0.25,  # Growth Stock
            "GOOGL": 0.20,  # Tech Stock
            "TSLA": 0.10,  # High Growth
            "BND": 0.05  # Some Bonds
        },
        "high": {
            "TSLA": 0.40,  # High Growth
            "AAPL": 0.30,  # Growth Stock
            "GOOGL": 0.20,  # Tech Stock
            "SPY": 0.10   # Market Index
        }
    }

    # Get the default allocation for the given risk level
    default_allocation = allocations.get(risk_level.lower(), allocations["medium"])

    # Adjust allocations based on user tickers
    final_allocation = {ticker: weight for ticker, weight in default_allocation.items() if ticker in tickers}

    # Normalize the weights to sum to 1
    total_weight = sum(final_allocation.values())
    final_allocation = {ticker: weight / total_weight for ticker, weight in final_allocation.items()}

    return final_allocation

if __name__ == "__main__":
    # Example user-defined tickers
    user_tickers = ["AAPL", "MSFT", "GOOGL", "TSLA", "SPY", "BND"]
    risk_choice = input("Enter risk level (low, medium, high): ").strip().lower()

    portfolio = get_portfolio_allocation(risk_choice, user_tickers)
    print("\nRecommended Portfolio Allocation:")
    print(pd.DataFrame.from_dict(portfolio, orient="index", columns=["Allocation %"]) * 100)