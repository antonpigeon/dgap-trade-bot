import requests
import pandas as pd
import plotly.graph_objects as go


def get_request(api_key: str, symbol='EUR/USD') -> dict:
    """

    :param api_key:
    :param symbol: Forex pairs
    :return: dict like {{'o': ..., 'h': ..., 'l': ..., 'c': ..., 'v': ..., 't': ..., 'tm': ..., }, {same dict}, ...}
      where o - open price [0]
            h - higher price [1]
            l - lower price [2]
            c - close price [3]
            tm - time [6]
    one sub_dict is the one candle
    """

    api_url = f'https://fcsapi.com/api-v3/forex/history?symbol={symbol}&id=1&period=1h&access_key={api_key}&level=3'
    response = requests.get(api_url)
    data = response.json()

    return data['response']


def create_table(data):
    """

    :param data: dict of subdicts with info about candles
    :return: DataFrame with prices of open and close of candlestick, higher and lower prices of candlestick
    """
    o = []
    h = []
    lo = []
    c = []
    time = []
    candles = []
    for key in data.keys():
        candles.append(data[key])
    for candle in candles:
        o.append(candle['o'])
        h.append(candle['h'])
        lo.append(candle['l'])
        c.append(candle['c'])
        time.append(candle['tm'])

    return pd.DataFrame(list(zip(o, h, lo, c, time)), columns=['open', 'higher', 'lower', 'close', 'time'])


def plot_chart(table):
    """

    :param table: type of this param is pd.DataFrame
    :return: figure, that we can show
    """
    return go.Figure(data=[go.Candlestick(x=table['time'], open=table['open'], high=table['higher'],
                                          low=table['lower'], close=table['close'])])
