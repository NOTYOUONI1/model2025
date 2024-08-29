import numpy as np
import pandas as pd
import pandas_ta as ta


def SuperTrend(data,length=10,multiplier=3):
    # Calculate SuperTrend
    sup = ta.supertrend(high=data['High'], low=data["Low"], close=data["Close"], length=length, multiplier=multiplier)

    # Convert to DataFrame and select the first column (SuperTrend values)
    sup = pd.DataFrame(sup)
    sup = sup[sup.columns[0]]

    # Reset index to avoid KeyError when dropping the first row
    sup.reset_index(drop=True, inplace=True)

    # Drop the first row after resetting the index
    sup.drop(index=0, inplace=True)

    # Drop NaN values
    sup.dropna(inplace=True, axis=0)

    # Align the index of the Close prices and SuperTrend values
    close_tail = data["Close"].tail(3).reset_index(drop=True)
    sup_tail = sup.tail(3).reset_index(drop=True)

    # Compare the last two Close prices with the last two SuperTrend values
    if sum(close_tail > sup_tail) == 3:
        return True
    else:
        return False

def calculate_rsi(data, length=14):
    # Calculate RSI using pandas_ta
    rsi = ta.rsi(data['Close'], length=length)

    if sum(rsi[-2:]<65)>0:
        if rsi.iloc[-2]<rsi.iloc[-1]:
            return [10, 0]
        else:
            return [0, 0]
    elif sum(rsi[-2:]>30)>0:
        if rsi[-2]>rsi[-1]:
            return [10, 0]
        else:
            return [0, 0]

def MACD_X(data,fast=12, slow=26, signal=9):
    # MACD হিসাব
    macd = data.ta.macd(close='Close', fast=12, slow=26, signal=9, append=True)

    # Drop NaN values to ensure clean data
    macd = macd.dropna()

    x = np.array(macd['MACD_12_26_9'])
    y = np.array(macd['MACDs_12_26_9'])
    distance = float(str(x[-1] - y[-1])[:7])
    print(distance)

    if distance>0.4 and distance<3:
        print("buy distance ok")
        if sum(x[-5:]>y[-5:])<2:
            return [10, 0],
        else:
            return [0, 0]
    elif distance<-0.4 and -3<distance:
        print("sell distance ok")
        if sum(x[-5:]<y[-5:])<2:
            return [0, 10]
        else:
            return [0, 0]
    else:
        print("else")
        return [0, 0]


def Bollinger_band(data, length, std):
    bb = ta.bbands(close=data["Close"], length=length, std=float(std))

    BBu=bb[f"BBU_{length}_{float(std)}"]
    BBl =bb[f"BBL_{length}_{float(std)}"]

    if sum(BBu.iloc[-3:]<data["Close"][-3:])>0:
        print("BB sell test:Ok")
        if sum(BBl.iloc[-7:]>data["Close"][-7:])>0:
            return [0, 20]
        else:
            return [0, 10]
    elif sum(BBl.iloc[-3:]>data["Close"][-3:])>0:
        print("BB buy test:Ok")
        if sum(BBu.iloc[-7:]<data["Close"][-7:])>0:
            return [20, 0]
        else:
            return [10, 0]
    else:
        print("BB Else test:Ok")
        return [0, 0]
