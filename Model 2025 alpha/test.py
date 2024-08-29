import matplotlib.pyplot as plt
import pandas as pd
import pandas_ta as ta
import yfinance as yf
import numpy as np
import time
# ডাটা ডাউনলোড


def MACD(data):
    # MACD হিসাব
    macd = data.ta.macd(close='Close', fast=12, slow=26, signal=9, append=True)

    # Drop NaN values to ensure clean data
    macd = macd.dropna()

    # Plot the MACD and Signal lines
    plt.plot(macd['MACD_12_26_9'], label='MACD')
    plt.plot(macd['MACDs_12_26_9'], label='Signal')
    plt.legend()
    plt.show()

    x = np.array(macd['MACD_12_26_9'])
    y = np.array(macd['MACDs_12_26_9'])
    distance = float(str(x[-1] - y[-1])[:7])
    print(distance)

    if distance>0.5 and distance<4:
        print("buy distance ok")
        if sum(x[-5:]>y[-5:])<2:
            return [10, 0],
        else:
            return [0, 0]
    elif distance<-0.5 and -4<distance:
        print("sell distance ok")
        if sum(x[-5:]<y[-5:])<2:
            return [0, 10]
        else:
            return [0, 0]
    else:
        print("else")
        return [0,0]


while True:
    time.sleep(30)
    data = yf.download('EURUSD=x', period='1d', interval='1m')
    v = MACD(data=data)
    print(v)