import pandas as pd
import numpy as np
import yfinance as yf
import  pandas_ta as ta

"""SuperTrade"""

data = yf.download('EURUSD=x', period="1d", interval="1m")
super = ta.m

print(super)