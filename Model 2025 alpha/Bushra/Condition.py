from admin_Info import open
import yfinance as yf
from DataSet_Manage import MongoDB
from Bot_Manage import MsgSend
from bson import ObjectId
from indecator import *

msg_sender = MsgSend(bot_token='7304471058:AAGyQcfuZXetXW4WdlFX6nDkkMK0IlCRt-U', group_chat_id=-1002249778339)
mongo = MongoDB(url=open["DayaSet Url"], db_name=open["DataSet Collection"])

def if_main(p):
    mongo_data = mongo.find_data(col="abra gabra")
    trade_id =mongo_data[0]["Number of trade"]

    data = yf.download(open["Symbol"], period="1d", interval="1m")
    if len(data)<600:
        data = yf.download(open["Symbol"], period="1d", interval="1m")
    print("Data fech Complete")
    print()


    superTrend = SuperTrend(data=data,length=open["Super Trende"]["length"], multiplier=open["Super Trende"]["multiplier"])
    RSI = calculate_rsi(data=data, length=open["RSI"]['length'])
    MACD = MACD_X(data=data,fast=open["MACD"]["fast"], slow=open["MACD"]["slow"], signal=open["MACD"]["signal"])
    BB = Bollinger_band(data=data, length=20, std=2)
    print(f"BB result={BB}")

    status = ""
    if p:
        buy_score = RSI[0]+MACD[0]+BB[0]
        sell_score = RSI[1]+MACD[1]+BB[1]

        buy_list = []
        sel_list = []


        if superTrend:
            buy_score+=10
            buy_list.append("Super Trend")
        elif not superTrend:
            sell_score+=10
            sel_list.append("Super Trend")


        if RSI==[10, 0]:
            buy_list.append("RSI")
        elif RSI==[0, 10]:
            sel_list.append("RSi")
        else:
            pass


        if MACD == [10, 0]:
            buy_list.append("MACD")
        elif MACD == [0, 10]:
            sel_list.append('MACD')
        else:
            pass

        print(f"Buy Score={buy_score} | Sell Score={sell_score} T")

        buy_score = (buy_score/30)*100
        sell_score = (sell_score/30)*100

        print(f"Buy Score={buy_score} | Sell Score={sell_score} H")

        if buy_score>sell_score:
            print("Buy")
            msg_sender.send_message(
                action="Buy",
                y="🍏",
                ask=data["Close"].iloc[-1],  # Access the last element using iloc
                trade_id=trade_id,
                HT=0,
                score=buy_score,
                st=buy_list
            )
        elif sell_score<sell_score:
            print("Sell")
            msg_sender.send_message(
                action="Sell",
                y="🍎",
                ask=data["Close"].iloc[-1],  # Access the last element using iloc
                trade_id=trade_id,
                HT=0,
                score=sell_score,
                st=sel_list
            )
        else:
            print("Hold")
            msg_sender.send_message(
                action="Hold",
                y="🤔",
                ask=data["Close"].iloc[-1],  # Access the last element using iloc
                trade_id=trade_id,
                HT=0,
                score=0,
                st="No"
            )

    mongo_data[0].pop("_id", None)
    mongo.update_data(col="abra gabra", old_data=mongo_data[0], new_data={"Number of trade":trade_id+1})