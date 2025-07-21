"""
칼럼 삭제
    df.drop("컬럼명", axis=1)
        원본은 그대로 유지되고 컬럼이 삭제된 새로운 데이터프레임 객체가 리턴됨
"""

import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC")
print(df) # 200 row x 6 columns

df2 = df.drop("volume", axis = 1) # 원본에 적용 x
print(df2)
print(df)

df3 = df.drop("volume", axis = 1, inplace=True) # 원본에 적용 O
print(df3)
print(df)