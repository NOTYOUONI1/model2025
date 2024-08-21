BOT_TOKEN = '7304471058:AAGyQcfuZXetXW4WdlFX6nDkkMK0IlCRt-U'
GROUP_CHAT_ID = -1002249778339

TICKER ='EURUSD=x'

MNT = 3

mongodb_url = "mongodb://localhost:27017"

bb_column = "Open"
bb_min_tuoch = 1
bb_lenght = 20
bb_std = 2
BBU = f"BBU_{bb_lenght}_{float(bb_std)}"
BBL = f"BBL_{bb_lenght}_{float(bb_std)}"
BBM = f"BBM_{bb_lenght}_{float(bb_std)}"


ask_column = "Close"

level_column = "Close"
threshold_percentage=0.1
min_touches=4
min_distance=15
min_d = 3.5

superT_length=7
superT_Mul =3.0
super_column = f"SUPERT_{superT_length}_{superT_Mul}"
min_super = 5


min_score = 60