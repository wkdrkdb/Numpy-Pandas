"""
사칙연산
    값은 인덱스를 기준으로 사칙 연산이 적용됨
    반복문을 사용하지 않아도 됨
"""

from pandas import Series

high = Series([51500, 51200, 52500, 51500, 51500])
low = Series([50700, 50500, 50500, 50800, 50700])
diff = high - low
print(diff)
"""
0     800   
1     700   
2    2000   
3     700   
4     800   
dtype: int64
"""

high = Series(data = [51500, 51200, 52500], index = ["5/1", "5/2", "5/3"])
low = Series(data = [50700, 50500, 50500], index = ["5/1", "5/2", "5/4"])
diff = high - low
print(diff)
"""
5/1    800.0
5/2    700.0
5/3      NaN
5/4      NaN
dtype: float64
"""