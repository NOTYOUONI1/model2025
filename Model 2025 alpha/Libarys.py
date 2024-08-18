import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from pymongo import MongoClient
import pandas_ta as ta


class Libary:
    def Get(self=0, symbol="EURUSD=x", period='1d', interval='1m', columns=None, scale=True):
        # Fetch stock data from Yahoo Finance
        data = yf.download(symbol, period=period, interval=interval)

        # Select specified columns if provided
        if columns:
            data = data[[columns]] if isinstance(columns, str) else data[columns]
        
        # Scale data using MinMaxScaler if required
        if scale:
            data = pd.DataFrame(MinMaxScaler().fit_transform(data), columns=data.columns, index=data.index)
        
        return data

    def Levels(self, data, threshold_percentage=0.1, min_touches=3, min_distance=0.5):
        levels = []
        prices = np.array(data)

        for i in range(len(prices)):
            level = prices[i]
            threshold = level * threshold_percentage / 100

            # Count touches within the threshold
            count = np.sum((prices >= level - threshold) & (prices <= level + threshold))

            # Add level if it has enough touches and isn't too close to existing levels
            if count >= min_touches and all(abs(level - l[0]) > min_distance for l in levels):
                levels.append((level, count))
        
        return levels

    def calculate_bollinger_bands(slef=0, data=None, length=20, std=2, append=True):

        data = pd.DataFrame(data, columns=["X"])
        data.ta.bbands(close='X', length=length, std=std, append=append)
        data.dropna(axis=0, inplace=True)

        return data