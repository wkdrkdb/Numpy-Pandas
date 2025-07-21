"""
시리즈 비교 연산
    비교 연산자의 결과로 Boolean 타입이 저장된 시리즈가 리턴 됨
"""

from pandas import Series

s = Series(data = [100, 200, 300, 400, 500])
cond = s > 300
print(cond)
"""
0    False
1    False
2    False
3     True
4     True
dtype: bool
"""