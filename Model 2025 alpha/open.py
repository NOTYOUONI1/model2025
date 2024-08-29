import pandas as pd
import yfinance as yf
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas_ta as ta
from main_if import main_if
import time


def xyx():
    data = pd.DataFrame(yf.download("EURUSD=x", period="1d", interval="1m"))
    if len(data)<601:
        data = pd.DataFrame(yf.download("EURUSD=x", period="5d", interval="1m"))
    data[:] = MinMaxScaler().fit_transform(data)

    bb = ta.bbands(close=data["Close"], length=20, std=2)

    # Generate buy/sell signals
    x = []
    for i in range(5, len(data), 10):
        for j in range(i, i + 5):
            if j < len(data):
                if data.iloc[j]["Close"] > bb.iloc[j]["BBU_20_2.0"]:
                    x.append((data.index[j], "Buy"))
                elif data.iloc[j]["Close"] < bb.iloc[j]["BBL_20_2.0"]:
                    x.append((data.index[j], "Sell"))

    # Evaluate signal performance
    y = []
    for i in x:
        idx = data.index.get_loc(i[0])
        if i[1] == "Buy":
            if data.iloc[idx - 1]["Close"]<data.iloc[idx + 4]["Close"]:
                y.append(1)
            else:
                y.append(0)
        else:
            if data.iloc[idx - 1]["Close"]>data.iloc[idx + 4]["Close"]:
                y.append(1)
            else:
                y.append(0)

    # Print performance metric
    return int(sum(y) / len(x) * 100)

while True:
    if xyx() > 60:
        for i in range(600):
            main_if()
            time.sleep(120)
    else:
        for i in range(600):
            main_if(bbP=False)
            time.sleep(120)
