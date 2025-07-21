"""
시계열 데이터와 인덱스
    시계열 데이터는 인덱스가 날짜와 시간으로 구성됨
        문자열로 표현된 날짜와 시간을 DatetimeIndex 타입으로 변환해서 사용해야 함
"""

import pandas as pd

date = ["2025-07-21", "2025-07-22"]
dt = pd.to_datetime(date)

print(type(date)) # list
print(type(dt)) # pandas.core.indexes.datetimes.DatetimeIndex
print(type(dt[0])) # pandas._libs.tslibs.timestamps.Timestamp