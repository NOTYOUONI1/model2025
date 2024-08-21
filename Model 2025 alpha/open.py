import pandas as pd
import numpy as np
import time
import traceback
from Libarys import Libary
from model_ac import *
from main_if import main_if
from sklearn.preprocessing import MinMaxScaler
import yfinance
import pandas_ta as ta
from database_M import MongoDB
from termcolor import colored
from bson import ObjectId

def tty_color(text, color):
    return colored(text, color)

mongo = MongoDB(url="mongodb://localhost:27017", db_name="M2025A")


def main():
    global Trades_id

    while True:
        try:
            # Fetch data
            data = yfinance.download(TICKER, period="1d", interval="1m")
            if len(data)<301:
                data = yfinance.download(TICKER, period="5d", interval="1m")
            if data is None or data.empty:
                raise ValueError("Failed to fetch data or data is empty")
            
            for i in data.columns:
                data[f"s_{i}"]= MinMaxScaler().fit_transform(data[[i]])

            # Bollinger Band
            bb = Libary.calculate_bollinger_bands(data=np.array(data[bb_column]))
            if bb is None or "X" not in bb.columns or BBU not in bb.columns or BBL not in bb.columns:
                raise ValueError("Bollinger Bands calculation returned unexpected results")
            Sell_bb = (bb["X"].tail(MNT) > bb[BBU].tail(MNT)).sum() > (bb_min_tuoch - 1)
            Buy_bb = (bb["X"].tail(MNT) < bb[BBL].tail(MNT)).sum() > (bb_min_tuoch - 1)

            # Find Support Resistance
            levels = Libary.Levels(self=0, data=data[level_column].tail(300))
            if not isinstance(levels, list) or not all(isinstance(t, tuple) for t in levels):
                raise ValueError("Libary.Levels did not return a list of tuples")
            x = data[level_column].iloc[-5:]
            closest_tuple = min(levels, key=lambda t: abs(t[0] - x.iloc[-1]))
            distance = abs(closest_tuple[0] - x.iloc[-1])
            Sell_level = (closest_tuple[0] > np.array(x)).sum() >= 3
            Buy_level = (closest_tuple[0] < np.array(x)).sum() >= 3
            print(f"Distance={distance} | Bollinger band buy={Buy_level} | Bollinger band Sell={Sell_bb}")

            # SuperTrend
            superT = Libary.supertrend(data=data, length=superT_length, multiplier=superT_Mul)
            super_Buy = sum(superT[super_column].iloc[-5:] < data["Open"].iloc[-5:]) > (min_super - 1)
            super_Sell = sum(superT[super_column].iloc[-5:] > data["Open"].iloc[-5:]) > (min_super - 1)
            print(f"Super Trade Buy={super_Buy} | Super Trade Sell={super_Sell}")

            # Moving Average
            lo = MinMaxScaler().fit_transform(data[["Close"]])
            lol = Libary.plot_moving_average(data=lo)
            lol_result = lo[-1] - lol.iloc[-1, 1]
            print(f"Lol Result={lol_result}")


            io, ichimoku_data = ta.ichimoku(high=data["s_High"], low=data["s_Low"], close=data["s_Close"], tenkan_sen=9, kijun_sen=26, senkou_span_b=52)

            io_green = io["ISA_9"].dropna(axis=0)
            io_red = io["ISB_26"].dropna(axis=0)


            HT = closest_tuple[1]
            ask = data[ask_column][-1]
            print(f"HT={HT}\nask={ask}")

            mongo_data=mongo.find_data(col="abra gabra")[0]
            Trades_id = mongo_data["Number of trade"]

            print(tty_color(text=f"Mongo data={mongo_data} | trade id={Trades_id}", color="red"))

            xyz = main_if(symbol=TICKER, sell_bb=Sell_bb, buy_bb=Buy_bb, sell_level=Sell_level, buy_level=Buy_level, HT=HT, ask=ask, trade_id=Trades_id, distance=distance, date_x=data.index[-1], super_buy=super_Buy, super_Sell=super_Sell, MV=lol_result, io_buy=io_green, io_sell=io_red, io_data=data["s_Close"])

            if xyz is False:
                break
            elif xyz is True:
                print(f"All oK={xyz}")


            mongo_data.pop("_id", None)
            print(tty_color(text=mongo_data, color="green"))
            mon = {"Number of trade":Trades_id+1}
            fgx = mongo.update_data(old_data=mongo_data, new_data=mon, col="abra gabra")
            if not fgx[0]==True:
                print(f"MongoBD ID Update Problam")
                break

            print(f"Trade Id={Trades_id}")
            time.sleep(180)

        except KeyboardInterrupt:
            print("Process was manually interrupted.")
            break
        except Exception as e:
            print(f"An error occurred in the main loop: {e}")
            traceback.print_exc()
            break

if __name__ == "__main__":
    main()