try:
                if distance < 3.5:
                if lower and less_count:
                    msg_sender.send_message(action="Buy", symbol=TICKER, y="🍏", ask=ask, trade_id=Trades_id, HT=closest_tuple[1], strategy="Bollinger Band Strategy + TCA")
                elif upper and greater_count:
                    msg_sender.send_message(action="Sell", symbol=TICKER, y="🍎", ask=ask, trade_id=Trades_id, HT=closest_tuple[1], strategy="Bollinger Band Strategy + TCA")
                elif less_count:
                    msg_sender.send_message(action="Buy", symbol=TICKER, y="🍏", ask=ask, trade_id=Trades_id, HT=closest_tuple[1], strategy="TCA")
                elif greater_count:
                    msg_sender.send_message(action="Sell", symbol=TICKER, y="🍎", ask=ask, trade_id=Trades_id, HT=closest_tuple[1], strategy="TCA")
                else:
                    msg_sender.send_message(action="Hold", symbol=TICKER, y="🤔", ask=ask, trade_id=Trades_id, HT=closest_tuple[1], strategy="Bollinger Band Strategy + TCA")
                

            if True:
                if lower:
                    msg_sender.send_message(action="Buy", symbol=TICKER, y="🍏", ask=ask, trade_id=Trades_id, HT=0, strategy="Bollinger Band Strategy")
                elif upper:
                    msg_sender.send_message(action="Sell", symbol=TICKER, y="🍎", ask=ask, trade_id=Trades_id, HT=0, strategy="Bollinger Band Strategy")
    except Exception as e:
    print(e)
