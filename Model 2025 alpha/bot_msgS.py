import telebot
import time

class MsgSend:
    def __init__(self, bot_token, group_chat_id):
        self.bot = telebot.TeleBot(bot_token)
        self.group_chat_id = group_chat_id
        self.emoji_map = {
            "Buy": "🚀💸",
            "Sell": "🚫💸",
            "Hold": "🤔🛑"
        }
        self.gif_url_map = {
            "Buy": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTZtYXBpaGxxdjNyZ2E5b2UyYWticnRiZDJ5Njk0a29qNmZ5ZjczZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JoeEHZjvkMiWFkMKV1/giphy.gif",
            "Sell": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGQ4NWZwNDFubGk1ZjkwcjhpZTRlMnZ1b3ZkMHl5Y2F5NjZsZG50YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ycqoq4xStjWRM9w7jl/giphy.gif",
            "Hold": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTQ3aWgxYjU0b2oyeHZ6cHdhMXR4dXF3cmxham5pYXd5bG1meTE2OSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RVaq71f1QGavKo239K/giphy.gif"
        }

    def send_message(self, action, symbol, y, ask, trade_id, HT, score, st):
        try:
            emoji = self.emoji_map.get(action, "🤔🛑")
            gif_url = self.gif_url_map.get(action, "https://media.giphy.com/media/3o7aD3nNmsDUoO2c5O/giphy.gif")

            message = (
                f"🤖 **Model 2025 Alpha** 🎯\n\n"
                f"**SYMBOL**: {symbol} 💲\n"
                f"**TIME**: {time.strftime('%Y-%m-%d %H:%M:%S')} ⏰\n"
                f"**{y} ACTION**: {action} {emoji}\n\n"
                f"**Ask Price**: {ask} 💵\n\n"
                f"**Horizontal Touch**: {HT} 🎯\n"
                f"**Trade ID**: {trade_id} 🆔\n"
                f"**Score__init**: {score}\n\n"
                f"**Strategy.s**: {st}\n\n"
                f"✨ May the odds be ever in your favor! ✨🍀"
            )

            self.bot.send_message(self.group_chat_id, message, parse_mode='Markdown')
            self.bot.send_animation(self.group_chat_id, gif_url)
        except Exception as e:
            print(f"Error sending message: {e}")