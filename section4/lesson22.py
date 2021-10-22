import altair as alt
import pandas as pd
import yfinance as yf

def get_data(days, tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = 'Name'
        df = pd.concat([df, hist])
    return df

days = 20
tickers = {
    'apple': 'AAPL',
    'facebook': 'FB',
    'google': 'GOOGL',
    'microsoft': 'MSFT',
    'netflix': 'NFLX',
    'amazon': 'AMZN'
}
abc = get_data(days, tickers)

companies = ['apple', 'facebook', 'amazon']
data = abc.loc[companies]
data = data.T.reset_index()
data = data.head()
data = pd.melt(data, id_vars=['Date']).rename(
    columns={'value': 'Stock Prices(USD)'}
)

print(data)