import pandas as pd
import yfinance as yf

aapl = yf.Ticker('AAPL')

days = 10
hist = aapl.history(period=f'{days}d').reset_index()
print(hist)

hist_msft = yf.Ticker('MSFT').history(period=f'{days}d').reset_index()
print(hist_msft.head())

print(pd.concat([hist, hist_msft], axis=1).head())