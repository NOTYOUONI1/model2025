import pandas as pd
import numpy as np
import time
import traceback
from Libarys import Libary
from model_ac import *
from main_if import main_if

Trades_id = 1


def main():
    global Trades_id

    while True:
        try:
            # Fetch data
            data = Libary.Get(self=0,symbol=TICKER, scale=False)

            # Calculate Bollinger Bands
            bb = Libary.calculate_bollinger_bands(data=np.array(data[bb_column]))
            if bb is None or "X" not in bb.columns or BBU not in bb.columns or BBL not in bb.columns:
                raise ValueError("Bollinger Bands calculation returned unexpected results")

            ask = data[ask_column][-1]

            # Get levels
            levels = Libary.Levels(self=0,data=data[level_column])
            if not isinstance(levels, list) or not all(isinstance(t, tuple) for t in levels):
                raise ValueError("Libary.Levels did not return a list of tuples")

            x = data[level_column][-5:]

            # Find closest tuple and calculate distance
            closest_tuple = min(levels, key=lambda t: abs(t[0] - x[-1]))
            distance = abs(closest_tuple[0] - x[-1])

            # Check conditions
            upper = (bb["X"].tail(MNT) > bb[BBU].tail(MNT)).sum() > (bb_min_tuoch - 1)
            lower = (bb["X"].tail(MNT) < bb[BBL].tail(MNT)).sum() > (bb_min_tuoch - 1)

            greater_count = (closest_tuple[0] > np.array(x)).sum() >= 3
            less_count = (closest_tuple[0] < np.array(x)).sum() >= 3

            HT = closest_tuple[1]

            xyz = main_if(symbol=TICKER, sell_bb=upper, buy_bb=lower, sell_level=greater_count, buy_level=less_count, HT=HT, ask=ask, trade_id=Trades_id, distance=distance, date_x=data.index[-1])
            
            if xyz == False:
                break
            

            # Print debug information
            print(distance)
            print("less_count", less_count)
            print("greater_count", greater_count)
            print("lower", lower)
            print("upper", upper)

            # Increment Trades_id and sleep
            Trades_id += 1
            time.sleep(MNT * 60)

        except Exception as e:
            print(f"An error occurred in main loop: {e}")
            traceback.print_exc()
            break

if __name__ == "__main__":
    main()
