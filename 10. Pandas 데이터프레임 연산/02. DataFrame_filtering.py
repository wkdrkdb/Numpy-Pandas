"""
데이터프레임 필터링
    비교 연산자의 결과를 Boolean 값을 갖고있는 시리즈 객체임
    예) 종가가 고가보다 높았던 거래일만 필터링 해보기
"""

import pyupbit
df = pyupbit.get_ohlcv_from("KRW-XRP")
print(df) # 2854 rows x 6 columns
 
cond = df["close"] > df["open"]
print(df[cond]) # 1357 rows x 6 columns

# 1357/2854 의 비율만큼 close > open