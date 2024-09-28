# this function will get market data for an array of ticker symbols
import numpy as np
import yfinance as yf
#init and finish dates must be of the form 'year-mm-dd'
def get_market_data (tickers, init, finish):
    for symbol in tickers:
        print(">>", symbol, end=" ... ")
        data = yf.download(symbol, start= init, end= finish)
        print(data)
    return
if __name__ =="__main__":
    symbols = ['AAPL', 'MSFT', 'VFINX', 'BTC-USD']
    get_market_data(symbols,'2020-09-25', '2020-10-02')