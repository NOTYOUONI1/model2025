import pandas as pd
import numpy as np
import time
from Libarys import Libary
from bot_msgS import MsgSend
from model_ac import *
from database_M import Dataset

Trades_id = 1

msg_sender = MsgSend(BOT_TOKEN, GROUP_CHAT_ID)

def main():
    global Trades_id

    while True:
        data = Libary.Get(self=0, symbol=TICKER, scale=False, columns="Open")
        data = np.array(data)
        bb = Libary.calculate_bollinger_bands(data=np.array(data))
        ask = data[-1]

        levels = Libary.Levels(self=0, data=data)
        x = data[-5:]

        closest_tuple = min(levels, key=lambda t: abs(t[0] - x[-1]))
        distance = abs(closest_tuple[0] - x[-1])

        upper = (bb["X"].tail(MNT) > bb["BBU_20_2.0"].tail(MNT)).sum() > 0
        lower = (bb["X"].tail(MNT) < bb["BBL_20_2.0"].tail(MNT)).sum() > 0

        greater_count = (closest_tuple[0] > x).sum() >= 3
        less_count = (closest_tuple[0] < x).sum() >= 3

        if distance < 3.5:
            if lower and less_count:
                msg_sender.send_message(action="Buy", symbol=TICKER, y="🍏", ask=ask, trade_id=Trades_id, HT=closest_tuple[1], strategy="Bollinger Band Strategy + TCA")
                Dataset(action="Buy", HT=closest_tuple[1], ask=ask, Symbol=TICKER, collection_name="single", st="Bollinger Band Strategy + TCA")
            elif upper and greater_count:
                msg_sender.send_message(action="Sell", symbol=TICKER, y="🍎", ask=ask, trade_id=Trades_id, HT=closest_tuple[1], strategy="Bollinger Band Strategy + TCA")
                Dataset(action="Sell", HT=closest_tuple[1], ask=ask, Symbol=TICKER, collection_name="single", st="Bollinger Band Strategy + TCA")
            elif less_count:
                msg_sender.send_message(action="Buy", symbol=TICKER, y="🍏", ask=ask, trade_id=Trades_id, HT=closest_tuple[1], strategy="TCA")
                Dataset(action="Buy", HT=closest_tuple[1], ask=ask, Symbol=TICKER, collection_name="single", st="TCA")
            elif greater_count:
                msg_sender.send_message(action="Sell", symbol=TICKER, y="🍎", ask=ask, trade_id=Trades_id, HT=closest_tuple[1], strategy="TCA")
                Dataset(action="Sell", HT=closest_tuple[1], ask=ask, Symbol=TICKER, collection_name="single", st="TCA")
            else:
                msg_sender.send_message(action="Hold", symbol=TICKER, y="🤔", ask=ask, trade_id=Trades_id, HT=closest_tuple[1], strategy="Bollinger Band Strategy + TCA")
                Dataset(action="Hold", HT=closest_tuple[1], ask=ask, Symbol=TICKER, collection_name="single", st="Bollinger Band Strategy + TCA")
        else:
            if lower:
                msg_sender.send_message(action="Buy", symbol=TICKER, y="🍏", ask=ask, trade_id=Trades_id, HT=0, strategy="Bollinger Band Strategy")
                Dataset(action="Buy", HT=0, ask=ask, Symbol=TICKER, collection_name="single", st="Bollinger Band Strategy")
            elif upper:
                msg_sender.send_message(action="Sell", symbol=TICKER, y="🍎", ask=ask, trade_id=Trades_id, HT=0, strategy="Bollinger Band Strategy")
                Dataset(action="Sell", HT=0, ask=ask, Symbol=TICKER, collection_name="single", st="Bollinger Band Strategy")
            else:
                msg_sender.send_message(action="Hold", symbol=TICKER, y="🤔", ask=ask, trade_id=Trades_id, HT=0, strategy="Bollinger Band Strategy")
                Dataset(action="Hold", HT=0, ask=ask, Symbol=TICKER, collection_name="single", st="Bollinger Band Strategy")

        print(distance)
        print()
        print("less_count", less_count)
        print()
        print("greater_count", greater_count)
        print()
        print("lower", lower)
        print()
        print("upper", upper)

        Trades_id += 1
        time.sleep(MNT * 60)

if __name__ == "__main__":
    main()
