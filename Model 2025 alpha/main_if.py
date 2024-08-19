from model_ac import *
from bot_msgS import MsgSend
from Libarys import Libary

msg_sender = MsgSend(BOT_TOKEN, GROUP_CHAT_ID)

def main_if(distance, sell_level, buy_level, buy_bb, sell_bb, HT, ask, trade_id, symbol, date_x):
    try:
        action = "Hold"
        if distance < 3.5:
            if sell_level and buy_bb:
                msg_sender.send_message(action="Buy", symbol=symbol, y="🍏", ask=ask, trade_id=trade_id, HT=HT, strategy="Bollinger Band Strategy + TCA")
                action = "Buy"
            elif sell_level and sell_bb:
                msg_sender.send_message(action="Sell", symbol=symbol, y="🍎", ask=ask, trade_id=trade_id, HT=HT, strategy="Bollinger Band Strategy + TCA")
                action = "Sell"
            elif buy_level:
                msg_sender.send_message(action="Buy", symbol=symbol, y="🍏", ask=ask, trade_id=trade_id, HT=HT, strategy="TCA")
                action = "Buy"
            elif sell_level:
                msg_sender.send_message(action="Sell", symbol=symbol, y="🍎", ask=ask, trade_id=trade_id, HT=HT, strategy="TCA")
                action = "Sell"
            else:
                msg_sender.send_message(action="Hold", symbol=symbol, y="🤔", ask=ask, trade_id=trade_id, HT=HT, strategy="Bollinger Band Strategy + TCA")
        
        if buy_bb:
            msg_sender.send_message(action="Buy", symbol=symbol, y="🍏", ask=ask, trade_id=trade_id, HT=0, strategy="Bollinger Band Strategy")
            action = "Buy"
        elif sell_bb:
            msg_sender.send_message(action="Sell", symbol=symbol, y="🍎", ask=ask, trade_id=trade_id, HT=0, strategy="Bollinger Band Strategy")
            action = "Sell"

        data = {
            "Symbol":symbol,
            "action":action,
            "ask":ask,
            "data":date_x
        }
        Libary.Mongodb(data=data, url=mongodb_url,db="M2025A",col="BackTest")
    except Exception as e:
        return False
    finally:
        return True
    
