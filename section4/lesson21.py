import yfinance as yf

aapl = yf.Ticker('AAPL')
aapl.actions.head()

print(aapl.dividends.plot())