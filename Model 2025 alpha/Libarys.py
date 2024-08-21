import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from pymongo import MongoClient
import pandas_ta as ta
import time as tm
import matplotlib.pyplot as plt
import numpy as np


class Libary:
    def Get(self=0, symbol="BTC-USD", period='1d', interval='1m', columns=None, scale=True):
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

    def backtest(real_data_index, real_data_price, result_data_index, result_data_price, result_data_action):
    # Convert input lists to numpy arrays
        r1 = np.array(real_data_index)
        r2 = np.array(real_data_price)
        d1 = np.array(result_data_index)
        d2 = np.array(result_data_price)  # Fixed the overwriting issue
        action = np.array(result_data_action)

    # Create a plot for real data prices
        plt.figure(figsize=(12, 6))
        plt.plot(r1, r2, label='Real Data Price', color='blue')

    # Plot vertical lines for Buy and Sell actions
        for i in range(len(result_data_index)):
            if action[i] == "Buy":
                plt.axvline(x=result_data_index[i], color='green', linestyle='--', linewidth=1, label='Buy Action' if i == 0 else "")
            else:
                plt.axvline(x=result_data_index[i], color='red', linestyle='--', linewidth=1, label='Sell Action' if i == 0 else "")

    # Add labels, legend, and title
        plt.xlabel('Index')
        plt.ylabel('Price')
        plt.title('Backtest Results')
        plt.legend(loc='best')
        plt.grid(True)
        plt.show()

    def supertrend(data, length, multiplier):
        df = pd.DataFrame(data)

        supertrend = ta.supertrend(df['High'], df['Low'], df['Close'], length=length, multiplier=multiplier)
        supertrend.drop(columns=supertrend.columns[-1], inplace=True)
        return supertrend
    def plot_moving_average(data,ma_type='SMA', period=20):

        data = pd.DataFrame(data, columns=["Close"])

        # Calculate the Moving Average (SMA or EMA)
        if ma_type == 'SMA':
            data['MA'] = data['Close'].rolling(window=period).mean()
        elif ma_type == 'EMA':
            data['MA'] = data['Close'].ewm(span=period, adjust=False).mean()
    
        return data