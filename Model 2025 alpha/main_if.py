from model_ac import *
from bot_msgS import MsgSend
from Libarys import Libary

msg_sender = MsgSend(BOT_TOKEN, GROUP_CHAT_ID)

def main_if(distance, sell_level, buy_level, buy_bb, sell_bb, HT, ask, trade_id, symbol, date_x, super_buy, super_Sell):
    try:
        action = "Hold"
        strategy = ""

        if distance < 3.5:
            if sell_level and buy_bb and super_buy:
                action = "Buy"
                strategy = "Bollinger Band Strategy + TCA"
            elif sell_level and sell_bb and super_Sell:
                action = "Sell"
                strategy = "Bollinger Band Strategy + TCA"
            elif buy_level and super_buy:
                action = "Buy"
                strategy = "TCA"
            elif sell_level and super_Sell:
                action = "Sell"
                strategy = "TCA"

        if buy_bb and super_buy:
            action = "Buy"
            strategy = "Bollinger Band Strategy"
            HT = 0
        elif sell_bb and super_Sell:
            action = "Sell"
            strategy = "Bollinger Band Strategy"
            HT = 0

        if action == "Buy":
            msg_sender.send_message(action="Buy", symbol=symbol, y="🍏", ask=ask, trade_id=trade_id, HT=HT, strategy=strategy)
        elif action == "Sell":
            msg_sender.send_message(action="Sell", symbol=symbol, y="🍎", ask=ask, trade_id=trade_id, HT=HT, strategy=strategy)
        else:
            msg_sender.send_message(action="Hold", symbol=symbol, y="🤔", ask=ask, trade_id=trade_id, HT=HT, strategy=strategy)

        data = {
            "Symbol": symbol,
            "action": action,
            "ask": ask,
            "data": date_x
        }
        Libary.Mongodb(data=data, url=mongodb_url, db="M2025A", col="BackTest")
    except Exception as e:
        return False
    finally:
        return True