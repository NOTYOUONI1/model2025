import numpy as np
import pandas as pd
import yfinance as yf
import pandas_ta as ta
from sklearn.preprocessing import MinMaxScaler

def download_data(symbol, period="1d", interval="1m", total_candles=400):
    try:
        data = yf.download(symbol, period=period, interval=interval)
        if len(data) < total_candles + 1:
            data = yf.download(symbol, period="5d", interval=interval)
        return data
    except Exception as e:
        print(f"Download Data Error: {e}")
        return pd.DataFrame()  # Return empty DataFrame if download fails

def preprocess_data(data):
    scaler = MinMaxScaler()
    for col in data.columns:
        data[col] = scaler.fit_transform(data[[col]])
    return data

def superTrade(data):
    try:
        length, multiplier = 10, 3.0
        supertrend = ta.supertrend(
            high=data['High'],
            low=data['Low'],
            close=data['Close'],
            length=length,
            multiplier=multiplier
        )
        supertrend = supertrend.rename(columns={f"SUPERT_{length}_{multiplier}": "SuperTrend"})
        result = data["Close"].iloc[-5:].mean() > supertrend["SuperTrend"].iloc[-5:].mean()
        return [(1, 0), "ST"] if result else [(0, 1), "ST"]
    except Exception as e:
        print(f"SuperTrade Error: {e}")
        return [(0, 1), "ST"]

def bollinger_band(data):
    try:
        length, std = 20, 2
        bb = ta.bbands(data["Close"], length=length, std=std, append=True)
        buy = sum(data["Close"].iloc[-3:] < bb[f"BBL_{length}_{float(std)}"].iloc[-3:]) > 0
        sell = sum(data["Close"].iloc[-3:] > bb[f"BBL_{length}_{float(std)}"].iloc[-3:]) > 0
        return [(1, 0), "BB"] if buy else [(0, 1), "BB"] if sell else [(0, 0), "BB"]
    except Exception as e:
        print(f"Bollinger Band Error: {e}")
        return [(1, 1), "BB"]

def support_resistance(data):
    global HT
    try:
        price_to_level = 0.1
        min_touches = 4
        min_distance = 0.5

        price = np.array(data['Close'])
        levels = []
        for level in price:
            touches = np.sum((price >= level - level * price_to_level / 100) & (price <= level + level * price_to_level / 100))
            if touches >= min_touches:
                if all(abs(level - l[0]) > min_distance for l in levels):
                    levels.append((level, touches))
        
        if not levels:
            raise ValueError("No levels found")

        last_prices = data['Close'].iloc[-5:].values
        closest_level = min(levels, key=lambda t: abs(t[0] - last_prices[-1]))
        closest_price, HT = closest_level

        Sell_level = np.sum(closest_price > last_prices) >= 3
        Buy_level = np.sum(closest_price < last_prices) >= 3

        return [(1, 0), "SR"] if Buy_level else [(0, 1), "SR"] if Sell_level else [(0, 0), "SR"]
    except Exception as e:
        print(f"Support Resistance Error: {e}")
        return [(1, 1), "SR"]

def ichimoku(data):
    try:
        tenkan_sen = 9
        kijun_sen = 26
        senkou_span_b = 52

        ichimoku_data, _ = ta.ichimoku(
            high=data["High"],
            low=data["Low"],
            close=data["Close"],
            tenkan_sen=tenkan_sen,
            kijun_sen=kijun_sen,
            senkou_span_b=senkou_span_b
        )

        ichimoku_data = ichimoku_data.rename(columns={
            f"ISA_{tenkan_sen}": "Ichimoku_A",
            f"ISB_{kijun_sen}": "Ichimoku_B"
        })
        ichimoku_data.dropna(axis=0, inplace=True)

        if len(data["Close"]) < 5 or len(ichimoku_data) < 5:
            raise ValueError("Not enough data for calculating Ichimoku values.")

        red_distance = abs(data["Close"].iloc[-5:].mean() - ichimoku_data["Ichimoku_B"].iloc[-5:].mean())
        green_distance = abs(data["Close"].iloc[-5:].mean() - ichimoku_data["Ichimoku_A"].iloc[-5:].mean())

        if red_distance < 1.9 or green_distance < 1.9:
            return [(1, 0), "Ichimoku"] if red_distance > green_distance else [(0, 1), "Ichimoku"]
        else:
            return [(0, 0), "Ichimoku"]
    except Exception as e:
        print(f"Ichimoku Error: {e}")
        return [(1, 1), "Ichimoku"]

def moving_average(data):
    try:
        period = 20
        mv = data["Close"].rolling(window=period).mean()
        o = (data["Close"].iloc[-1] - mv.iloc[-1]) * 100

        return [(1, 0), "MA"] if o < 2.1 else [(0, 1), "MA"] if o > 2.1 else [(0, 0), "MA"]
    except Exception as e:
        print(f"Moving Average Error: {e}")
        return [(1, 1), "MA"]

def main():
    symbol = 'EURUSD=x'
    par_candle_power = "1m"
    total_candle_s = 400
    
    data = download_data(symbol, period="1d", interval=par_candle_power, total_candles=total_candle_s)
    
    if data.empty:
        print("No data available. Exiting.")
        return

    data = preprocess_data(data)
    
    global HT
    HT = None

    results = {
        "SuperTrade": superTrade(data)[0],
        "Bollinger Band": bollinger_band(data)[0],
        "Support Resistance": support_resistance(data)[0],
        "Ichimoku": ichimoku(data)[0],
        "Moving Average": moving_average(data)[0],
        "HT": HT,
        "ask":data["Close"][-1]
    }

    print("Results:", results)

    return results

if __name__ == "__main__":
    main()
