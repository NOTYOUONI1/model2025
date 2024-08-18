import telebot
import time

class MsgSend:
    def __init__(self, bot_token, group_chat_id):
        self.bot = telebot.TeleBot(bot_token)
        self.group_chat_id = group_chat_id

    def send_message(self, action, symbol, y, ask, trade_id, HT, strategy):
        # Define emojis for actions
        emoji_map = {
            "Buy": "🚀💸",
            "Sell": "🚫💸",
            "Hold": "🤔🛑"
        }
        emoji = emoji_map.get(action, "🤔🛑")

        # Construct the message with enhanced emojis
        message = (
            f"🤖 **Model 2025 Alpha** 🎯\n\n"
            f"**SYMBOL**: {symbol} 💲\n"
            f"**TIME**: {time.strftime('%Y-%m-%d %H:%M:%S')} ⏰\n"
            f"**{y} ACTION**: {action} {emoji}\n\n"
            f"**Ask Price**: {ask} 💵\n\n"
            f"**Horizontal Touch**: {HT} 🎯\n"
            f"**Trade ID**: {trade_id} 🆔\n"
            f"**Strategy**: {strategy} 🧠\n\n"
            f"✨ May the odds be ever in your favor! ✨🍀"
        )

        # Send the message to the group chat
        self.bot.send_message(self.group_chat_id, message, parse_mode='Markdown')

        # Send a funny or cute GIF based on action
        gif_url_map = {
            "Buy": "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",  # Example GIF for Buy
            "Sell": "https://media.giphy.com/media/3orieY3MhT8CAqX7nO/giphy.gif",  # Example GIF for Sell
            "Hold": "https://media.giphy.com/media/l1J9ACblVmcAa5O3S/giphy.gif"   # Example GIF for Hold
        }
        gif_url = gif_url_map.get(action, "https://media.giphy.com/media/3o7aD3nNmsDUoO2c5O/giphy.gif")

        self.bot.send_animation(self.group_chat_id, gif_url)

# Example usage:
"""msg_sender = MsgSend(BOT_TOKEN, GROUP_CHAT_ID)
msg_sender.send_message("Buy", "AAPL", "🍏", 150.25, 1, 3, "Bollinger Band Strategy")"""
