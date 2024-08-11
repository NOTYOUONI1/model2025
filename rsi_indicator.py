import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt

# Example price data
prices = pd.Series(data["Close"])

# Calculate RSI
rsi = ta.rsi(prices, length=14)

print("RSI Values:")
print(rsi)

plt.figure(figsize=(20, 5))
plt.plot(rsi)
plt.grid()

# Add horizontal lines for RSI levels 10, 20, 30, ..., 100
for i in range(10, 110, 10):
    plt.axhline(y=i, color='gray', linestyle='--', alpha=0.2)

plt.show()
