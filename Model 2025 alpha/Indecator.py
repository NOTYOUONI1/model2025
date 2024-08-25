import numpy as np
import pandas as pd
import yfinance as yf
import pandas_ta as ta
from open import open
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
            return [(1, 0), "ST"]
        elif sell_signal:
            return [(0, 1), "ST"]
        else:
            return [(0, 0), "ST"]

    except Exception as e:
        # Print the error message and return a default value
        print(f"SuperTrade Error: {e}")
        return [(1, 1), "ST"]


def bollinger_band(data):
    try:
        length = open["bollinger_band"]["length"]
        std = open["bollinger_band"]["std"]

        bb = ta.bbands(data["Close"], length=length, std=std, append=True)
        buy = sum(data["Close"].iloc[-3:] < bb[f"BBL_{length}_{float(std)}"].iloc[-3:]) > open["bollinger_band"]["Min"]
        sell = sum(data["Close"].iloc[-3:] > bb[f"BBU_{length}_{float(std)}"].iloc[-3:]) > open["bollinger_band"]["Min"]
        return [(1, 0), "BB"] if buy else [(0, 1), "BB"] if sell else [(0, 0), "BB"]
    except Exception as e:
        print(f"Bollinger Band Error: {e}")
        return [(1, 1), "BB"]


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

        return [(1, 0), HT] if Buy_level else [(0, 1), HT] if Sell_level else [(0, 0), 0]
    except Exception as e:
        print(f"Support Resistance Error: {e}")
        return [(1, 1), "SR"]


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
            return [(1, 0), "Ichimoku"] if red_distance > green_distance else [(0, 1), "Ichimoku"]
        else:
            return [(0, 0), "Ichimoku"]
    except Exception as e:
        print(f"Ichimoku Error: {e}")
        return [(1, 1), "Ichimoku"]


def moving_average(data):
    try:
        period = open["moving_average"]["period"]
        mv = data["Close"].rolling(window=period).mean()
        o = (data["Close"].iloc[-1] - mv.iloc[-1]) * 100

        if o > open["moving_average"]["Min"]:
            if mv[-4:].mean() > data["Close"][-4:].mean():
                return [(1, 0), 'MA']
            else:
                return [(0, 1), 'MA']
        else:
            return [(0, 0), "MA"]
    except Exception as e:
        print(f"Moving Average Error: {e}")
        return [(1, 1), "MA"]


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
        "SuperTrade": superTrade(data)[0],
        "Bollinger Band": bollinger_band(data)[0],
        "Support Resistance": v[0],
        "Ichimoku": ichimoku(data)[0],
        "Moving Average": moving_average(data)[0],
        "HT": v[1],
        "ask": ask,
        "Symbol": open["Symbol"]
    }

    print("Results:", results)

    return results


if __name__ == "__main__":
    print("Call Indicator file")
    main()  # Added the missing call to `main()`
