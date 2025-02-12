import numpy as np
import pandas as pd

def monte_carlo_simulation(stock_data, num_simulations=100, time_horizon=252):
    """
    Perform Monte Carlo simulations to estimate future stock prices.
    """
    log_returns = np.log(stock_data / stock_data.shift(1)).dropna()
    mean_return = log_returns.mean()
    std_dev = log_returns.std()

    simulation_results = {}

    for ticker in stock_data.columns:
        last_price = stock_data[ticker].iloc[-1]
        simulations = np.zeros((num_simulations, time_horizon))

        for i in range(num_simulations):
            price_series = [last_price]
            for _ in range(time_horizon):
                random_return = np.random.normal(mean_return[ticker], std_dev[ticker])
                new_price = price_series[-1] * np.exp(random_return)
                price_series.append(new_price)

            simulations[i, :] = price_series[1:]  

        simulation_results[ticker] = simulations

    return simulation_results
