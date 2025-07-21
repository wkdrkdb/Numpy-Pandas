import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC")
print(df) # 200 row x 6 columns

df["range"] = df["high"] - df["low"]
print(df.head())