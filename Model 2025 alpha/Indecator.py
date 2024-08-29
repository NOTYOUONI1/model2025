import numpy as np
import pandas as pd
import yfinance as yf
import pandas_ta as ta
from admin import open
from sklearn.preprocessing import MinMaxScaler


def download_data(symbol, period="1d", interval="1m", total_candles=600):
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
    data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns, index=data.index)
    return data


def superTrade(data):
    try:
        length = open["Super Trende"]["length"]
        multiplier = open["Super Trende"]["multiplier"]

        supertrend = ta.supertrend(
            high=data['High'],
            low=data['Low'],
            close=data['Close'],
            length=length,
            multiplier=multiplier
        )

        # Rename the SuperTrend column
        supertrend = supertrend.rename(columns={f"SUPERT_{length}_{multiplier}": "SuperTrend"})

        # Determine buy and sell signals based on SuperTrend
        buy_signal = data["Close"].iloc[-5:].mean() > supertrend["SuperTrend"].iloc[-5:].mean()
        sell_signal = data["Close"].iloc[-5:].mean() < supertrend["SuperTrend"].iloc[-5:].mean()

        # Return the appropriate result based on the signals
        if buy_signal:
            return [True, False], "ST"
        elif sell_signal:
            return [False, True], "ST"
        else:
            return [False, False], "ST"

    except Exception as e:
        # Print the error message and return a default value
        print(f"SuperTrade Error: {e}")
        return [True, True], "ST"


def bollinger_band(data):
    try:
        length = open["bollinger_band"]["length"]
        std = open["bollinger_band"]["std"]

        bb = ta.bbands(data["Close"], length=length, std=std, append=True)
        buy = sum(data["Close"].iloc[-3:] < bb[f"BBL_{length}_{float(std)}"].iloc[-3:]) > open["bollinger_band"]["Min"]
        sell = sum(data["Close"].iloc[-3:] > bb[f"BBU_{length}_{float(std)}"].iloc[-3:]) > open["bollinger_band"]["Min"]
        return [True, False], "BB" if buy else [False, True], "BB" if sell else [False, False], "BB"
    except Exception as e:
        print(f"Bollinger Band Error: {e}")
        return [True, True], "BB"


def support_resistance(data):
    try:
        price_to_level = open["support_resistance"]["price_to_level"]
        min_touches = open["support_resistance"]["min_touches"]
        min_distance = open["support_resistance"]["min_distance"]

        price = np.array(data['Close'][open["support_resistance"]["Last Cande no."]:])
        levels = []
        for level in price:
            touches = np.sum(
                (price >= level - level * price_to_level / 100) & (price <= level + level * price_to_level / 100))
            if touches >= min_touches:
                if all(abs(level - l[0]) > min_distance for l in levels):
                    levels.append((level, touches))

        if not levels:
            raise ValueError("No levels found")

        last_prices = data['Close'].iloc[-5:].values
        closest_level = min(levels, key=lambda t: abs(t[0] - last_prices[-1]))
        closest_price, HT = closest_level

        Sell_level = np.sum(closest_price > last_prices) >= open["support_resistance"]["Min"]
        Buy_level = np.sum(closest_price < last_prices) >= open["support_resistance"]["Min"]

        return [True, False], HT if Buy_level else [False, True], HT if Sell_level else [False, False], 0
    except Exception as e:
        print(f"Support Resistance Error: {e}")
        return [True, True], "SR"


def ichimoku(data):
    try:
        tenkan_sen = open["ichimoku"]["tenkan_sen"]
        kijun_sen = open["ichimoku"]["kijun_sen"]
        senkou_span_b = open["ichimoku"]["senkou_span_b"]

        ichimoku_data, _ = ta.ichimoku(
            high=data["High"],
            low=data["Low"],
            close=data["Close"],
            tenkan=tenkan_sen,
            kijun=kijun_sen,
            senkou=senkou_span_b
        )

        ichimoku_data = ichimoku_data.rename(columns={
            f"ISA_{tenkan_sen}": "Ichimoku_A",
            f"ISB_{kijun_sen}": "Ichimoku_B"
        })
        ichimoku_data.dropna(axis=0, inplace=True)

        red_distance = abs(data["Close"].iloc[-5:].mean() - ichimoku_data["Ichimoku_B"].iloc[-5:].mean())
        green_distance = abs(data["Close"].iloc[-5:].mean() - ichimoku_data["Ichimoku_A"].iloc[-5:].mean())

        if red_distance < open["ichimoku"]["Min Distance"] or green_distance < open["ichimoku"]["Min Distance"]:
            return [True, False], "Ichimoku" if red_distance > green_distance else [False, True], "Ichimoku"
        else:
            return [False, False], "Ichimoku"
    except Exception as e:
        print(f"Ichimoku Error: {e}")
        return [True, True], "Ichimoku"


def moving_average(data):
    try:
        period = open["moving_average"]["period"]
        mv = data["Close"].rolling(window=period).mean()
        o = (data["Close"].iloc[-1] - mv.iloc[-1]) * 100

        if o > open["moving_average"]["Min"]:
            if mv[-4:].mean() > data["Close"][-4:].mean():
                return [True, False], 'MA'
            else:
                return [False, True], 'MA'
        else:
            return [False, False], "MA"
    except Exception as e:
        print(f"Moving Average Error: {e}")
        return [True, True], "MA"
def macd_signal(data):
    try:
        data['EMA12'] = data['Close'].ewm(span=12, adjust=False).mean()
        data['EMA26'] = data['Close'].ewm(span=26, adjust=False).mean()
        data['MACD'] = data['EMA12'] - data['EMA26']
        data['Signal'] = data['MACD'].ewm(span=9, adjust=False).mean()
        data['Histogram'] = data['MACD'] - data['Signal']
        data['Histogram_Percentage'] = data['Histogram'] * 10000

        last_histogram = data["Histogram_Percentage"].iloc[-1]

        # Improved distance calculation
        if data["Signal"][-1] != 0:
            distance = (data["MACD"][-1] - data["Signal"][-1]) / data["Signal"][-1] * 100
        else:
            distance = 0

        print(f"Last Histogram: {last_histogram}, Distance: {distance}")

        if distance < 9:
            return [False, False], "MACD", last_histogram
        else:
            if last_histogram > 10:
                return [True, False], "MACD", last_histogram
            elif last_histogram < -10:
                return [False, True], "MACD", last_histogram
            else:
                return [True, False], "MACD", last_histogram
    except Exception as e:
        print(f"MACD==Error: {e}")
        return [True, True], "MACD", distance



def main():
    par_candle_power = open["Par Candle Power"]
    total_candle_s = open["Min Total Candle"]

    data = download_data(open["Symbol"], period="1d", interval=par_candle_power, total_candles=total_candle_s)

    ask = data["Close"][-1]

    if data.empty:
        print("No data available. Exiting.")
        return

    data = preprocess_data(data=data)

    v = support_resistance(data)

    results = {
        "SuperTrade": superTrade(data),
        "Bollinger Band": bollinger_band(data),
        "Support Resistance": v,
        "Ichimoku": ichimoku(data),
        "Moving Average": moving_average(data),
        "MACD":macd_signal(data),
        "HT": v[1],
        "ask": ask,
        "Symbol": open["Symbol"]
    }

    print("Results:", results)

    return results


if __name__ == "__main__":
    print("Call Indicator file")
    main()  # Added the missing call to `main()`