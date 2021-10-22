import pandas as pd
import yfinance as yf

aapl = yf.Ticker('AAPL')

days = 15
hist = aapl.history(period=f'{days}d')
hist_msft = yf.Ticker('MSFT').history(period=f'{days}d').reset_index()

hist.index = hist.index.strftime('%d %B %Y')

hist = hist[['Close']]

hist.columns = ['apple']
hist = hist.T
hist.index.name = 'Name'

print(hist)