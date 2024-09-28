import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

stock_data = yf.download('IGE', start= '2001-11-26', end= '2007-11-15').dropna()  #pulls in IGE data over 6 year window from yahoo finance
stock_data = stock_data['Close']
stock_data.head()


benchmark_data = yf.download('^GSPC', start='2001-11-26', end= '2007-11-15').dropna()#pulls in the Global Standard and poor's composite data over 6 year window from yahoo finance
benchmark_data = benchmark_data[['Close']].rename(columns={'Close': 'S&P 500'})# pulls the close values over the 6 year window for the s&p 500
benchmark_data.head()


stock_returns = stock_data.pct_change() #computes percent daily change of the closing price
sp_returns = benchmark_data['S&P 500'].pct_change()#computes percent daily change of the closing price

excess_returns = stock_returns.sub(sp_returns, axis=0).dropna() #This line computes the difference between stock_returns and sp_returns for each corresponding day.
avg_excess_return = excess_returns.mean()
std_excess_return = excess_returns.std()
daily_sharpe_ratio = avg_excess_return / std_excess_return
annual_factor = np.sqrt(252) #there are 252 trading days in one year
annual_sharpe_ratio = daily_sharpe_ratio*annual_factor
print(annual_sharpe_ratio)