"""
로우 추가
    loc 속성을 사용
        df.loc[인덱스] = 데이터
"""
import pyupbit
import pandas as pd

df = pyupbit.get_ohlcv("KRW-BTC")
print(df)

df.drop(["volume", "value"], axis = 1, inplace = True)
print(df)

date = "2025-07-21 09:00:00"
dt = pd.to_datetime(date)
print(dt) # 2025-07-21 09:00:00

df.loc[dt] = [100, 110, 100, 100]
print(df)