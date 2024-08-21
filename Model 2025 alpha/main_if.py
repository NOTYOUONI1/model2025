from model_ac import *
from bot_msgS import MsgSend
from Libarys import Libary
from sklearn.preprocessing import MinMaxScaler
from database_M import MongoDB


def tty_color(text, color):
    """
    Apply color to the terminal text.

    :param text: The text to be colored.
    :param color: The color code for the text.
                   Examples of color codes:
                   30 = Black
                   31 = Red
                   32 = Green
                   33 = Yellow
                   34 = Blue
                   35 = Magenta
                   36 = Cyan
                   37 = White
    :return: The colored text.
    """
    # ANSI escape code for text color
    return f"\033[38;5;{color}m{text}\033[0m"


msg_sender = MsgSend(BOT_TOKEN, GROUP_CHAT_ID)

def main_if(distance, sell_level, buy_level, buy_bb, sell_bb, HT, ask, trade_id, symbol, date_x, super_buy, super_Sell, MV, io_buy, io_sell, io_data):
    try:
        action = "Hold"
        buy_result, sell_result = 0, 0
        buy_result_list, sell_result_list = [], []

        # Calculate differences and determine action based on Ichimoku Cloud
        diff_buy, diff_sell = abs(io_buy.iloc[-1] - io_data[-1])*100, abs(io_sell.iloc[-1] - io_data[-1])*100
        print(tty_color(text=f"diff_buy={diff_buy} | diff_sell={diff_sell}", color=32))

        if diff_buy < 1.9 or diff_sell < 1.9:
            if diff_sell > diff_buy and sum(io_buy[-5:] < io_data[-5:]) > 3:
                buy_result += 10
                buy_result_list.append("Ichimoku")
            elif sum(io_sell[-5:] > io_data[-5:]) > 3:
                sell_result += 10
                sell_result_list.append("Ichimoku")
        elif diff_sell > diff_buy:
            if sum(io_buy[-5:] < io_data[-5:]) == 5:
                sell_result += diff_sell/10
                sell_result_list.append(f"Ichimoku{diff_sell}")
        elif sum(io_sell[-5:] > io_data[-5:]) == 5:
            buy_result += diff_buy/10
            buy_result_list.append(f"Ichimoku{diff_buy}")

        # Process other indicators
        if distance < min_d:
            buy_result += 10
            sell_result += 10
            buy_result_list.append("Distance")
            sell_result_list.append("Distance")
        if buy_level:
            buy_result += 10
            buy_result_list.append("Level")
        if buy_bb:
            buy_result += 10
            buy_result_list.append("BB")
        if super_buy:
            buy_result += 10
            buy_result_list.append("Super Trade")
        if MV > 2.5:
            buy_result += MV * 5
            buy_result_list.append(f"MV {MV}")
        if sell_bb:
            sell_result += 10
            sell_result_list.append("BB")
        if sell_level:
            sell_result += 10
            sell_result_list.append("Level")
        if super_Sell:
            sell_result += 10
            sell_result_list.append("Super Trade")
        if MV < -2.5:
            sell_result += abs(MV * 5)
            sell_result_list.append(f"MV {MV}")

        # Normalize and compare results
        buy_result = (buy_result / 55) * 100
        sell_result = (sell_result / 55) * 100

        if max(buy_result, sell_result) > min_score:
            if buy_result > sell_result:
                msg_sender.send_message(action="Buy", symbol=symbol, y="🍏", ask=ask, trade_id=trade_id, HT=HT, score=buy_result, st=buy_result_list)
                action = "Buy"
            else:
                msg_sender.send_message(action="Sell", symbol=symbol, y="🍎", ask=ask, trade_id=trade_id, HT=HT, score=sell_result, st=sell_result_list)
                action = "Sell"


        print(f"buy Score {buy_result} | Sell Score {sell_result}")

        # Log to MongoDB
        data = {"Symbol": symbol, "action": action, "ask": ask, "data": date_x, "buy Score": buy_result, "Sell result": sell_result}
        MongoDB(url="mongodb://localhost:27017", db_name="M2025A").insert_data(data=data,col="BackTest")

    except Exception as e:
        print(f"Error: {e}")
        return False
    return True
