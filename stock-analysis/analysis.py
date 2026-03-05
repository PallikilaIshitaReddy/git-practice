import pandas as pd
import numpy as np

# Load stock data
df = pd.read_csv("stock_data.csv")

# Calculate daily returns
df["Daily Return"] = df["Close"].pct_change()

# Calculate moving averages
df["MA20"] = df["Close"].rolling(window=20).mean()
df["MA50"] = df["Close"].rolling(window=50).mean()

# Generate trading signals
df["Signal"] = np.where(df["MA20"] > df["MA50"], "BUY", "SELL")

# Summary statistics
average_return = df["Daily Return"].mean()
volatility = df["Daily Return"].std()

print("Average Daily Return:", average_return)
print("Volatility (Risk):", volatility)

print("\nLast 5 Trading Signals:")
print(df[["Close", "MA20", "MA50", "Signal"]].tail())