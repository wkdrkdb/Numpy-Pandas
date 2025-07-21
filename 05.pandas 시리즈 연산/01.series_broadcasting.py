"""
브로드캐스팅(Broadcasting)
    연산이 시리즈 객체의 전체 값에 적용됨
    반복문을 사용하지 않음
"""

from pandas import Series

s = Series([100, 200, 300])
print(s + 10)
"""
0    110
1    210
2    310
dtype: int64
"""
