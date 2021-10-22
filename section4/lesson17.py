import pandas as pd
import yfinance as yf

aapl = yf.Ticker('AAPL')

days = 15
hist = aapl.history(period=f'{days}d') 
print(hist)