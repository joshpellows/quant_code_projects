
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Download stock data
stock_data = yf.download('IGE', start='2001-11-26', end='2010-11-15').dropna()
print("Stock Data (Head):")
print(stock_data.head())  # Debugging: Check first few rows of stock data
stock_data = stock_data['Close']  # Use the 'Close' column for stock data

# Download benchmark (S&P 500) data
benchmark_data = yf.download('^GSPC', start='2001-11-26', end='2010-11-15').dropna()
print("Benchmark Data (Head):")
print(benchmark_data.head())  # Debugging: Check first few rows of benchmark data
benchmark_data = benchmark_data[['Close']].rename(columns={'Close': 'S&P 500'})  # Use 'Close' column for benchmark

# Align stock data and benchmark data by their index (date)
combined_data = pd.concat([stock_data, benchmark_data['S&P 500']], axis=1, join='inner')

# Check the combined data's columns
print("Combined Data Columns:")
print(combined_data.columns)

# Calculate returns
stock_returns = combined_data['IGE'].pct_change()  # Use 'IGE' for stock returns
sp_returns = combined_data['^GSPC'].pct_change()  # Use 'S&P 500' for benchmark returns

# Check returns for NaN values
print("Stock Returns (Head):")
print(stock_returns.head())  # Debugging: Check first few rows of stock returns

print("S&P 500 Returns (Head):")
print(sp_returns.head())  # Debugging: Check first few rows of S&P 500 returns

# Calculate excess returns
excess_returns = stock_returns.sub(sp_returns, axis=0).dropna()

# Check excess returns for NaN values
print("Excess Returns (Head):")
print(excess_returns.head())  # Debugging: Check first few rows of excess returns

# Calculate the average and standard deviation of excess returns
avg_excess_return = excess_returns.mean()
std_excess_return = excess_returns.std()

# Calculate the daily and annual Sharpe ratios
daily_sharpe_ratio = avg_excess_return / std_excess_return
annual_factor = np.sqrt(252)  # 252 trading days in a year
annual_sharpe_ratio = daily_sharpe_ratio * annual_factor

# Print the annual Sharpe ratio
print(f"Annual Sharpe Ratio: {annual_sharpe_ratio}")
