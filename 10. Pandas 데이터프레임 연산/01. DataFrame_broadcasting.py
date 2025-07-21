"""
브로드캐스팅
    하나의 연산이 한 컬럼의 모든 데이터에 적용됨
"""

import pyupbit

df = pyupbit.get_ohlcv_from("KRW-XRP")
print(df)

print(df["open"] + 100)