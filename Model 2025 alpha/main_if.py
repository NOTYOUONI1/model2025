from bot_msgS import MsgSend
from database_M import MongoDB
from Indecator import main
from Tool import *
from bson import ObjectId
from model_ac import *
import time

# Initialize message sender and MongoDB
msg_sender = MsgSend(BOT_TOKEN, GROUP_CHAT_ID)
mongo_db = MongoDB(url="mongodb://localhost:27017", db_name="M2025A")

# Retrieve data from MongoDB
mongo_data = mongo_db.find_data(col="abra gabra")[0]
trade_id = mongo_data["Number of trade"]

def main_if():
    try:
        action = "Hold"
        buy_result, sell_result = 0, 0
        buy_result_list, sell_result_list = [], []

        # Get the trading data
        data = main()

        Symbol = data["Symbol"]
        HT = data["HT"]

        # Process SuperTrade
        if bool(data["SuperTrade"][1]):
            sell_result += 10
            sell_result_list.append("ST")
        elif bool(data["SuperTrade"][0]):
            buy_result += 10
            buy_result_list.append("ST")

        # Process Bollinger Band
        if bool(data["Bollinger Band"][1]):
            sell_result += 10
            sell_result_list.append("BB")
        elif bool(data["Bollinger Band"][0]):
            buy_result+=10
            buy_result_list.append("BB")

        # Process Support Resistance
        if bool(data["Support Resistance"][1]):
            sell_result += 10
            sell_result_list.append("SR")
        elif bool(data["Support Resistance"][0]):
            buy_result += 10
            buy_result_list.append("SR")

        if bool(data["Ichimoku"][1]):
            sell_result += 10
            sell_result_list.append("IC")
        elif bool(data['Ichimoku'][0]):
            buy_result += 10
            buy_result_list.append("IC")

        if bool(data["Moving Average"][1]):
            sell_result += 10
            sell_result_list.append("MA")
        elif bool(data["Moving Average"][0]):
            buy_result += 10
            buy_result_list.append("MA")



        buy_result = (buy_result / 50) * 100
        sell_result = (sell_result / 50) * 100

        if max(buy_result, sell_result) > min_score:
            if buy_result > sell_result:
                msg_sender.send_message(action="Buy", symbol=Symbol, y="🍏", ask=data["ask"], trade_id=trade_id, HT=HT, score=buy_result, st=buy_result_list)
                action = "Buy"
            elif buy_result<sell_result:
                msg_sender.send_message(action="Sell", symbol=Symbol, y="🍎", ask=data["ask"], trade_id=trade_id, HT=HT, score=sell_result, st=sell_result_list)
                action = "Sell"
            else:
                msg_sender.send_message(action="Hold", symbol=Symbol, y="🤔", ask=data['ask'], trade_id=trade_id, HT=HT, score=0, st=0)
                action = "Hold"    
        else:
            msg_sender.send_message(action="Hold", symbol=Symbol, y="🤔", ask=data['ask'], trade_id=trade_id, HT=HT, score=0, st=0)
            action = "Hold"

        print(tty_color(text=f"Buy Score: {buy_result} | Sell Score: {sell_result}", color="red"))

        """
        log_data = {
            "Symbol": Symbol,
            "action": action,
            "ask": data["ask"],
            "data": 0,
            "buy Score": buy_result,
            "Sell result": sell_result
        }
        mongo_db.insert_data(data=log_data, col="BackTest")"""
        mongo_data.pop("_id", None)
        mongo_db.update_data(old_data=mongo_data, new_data={"Number of trade": trade_id + 1}, col="abra gabra")

    except Exception as e:
        print(f"Error: {e}")
        return False
    return True

while True:
    main_if()
    time.sleep(180)