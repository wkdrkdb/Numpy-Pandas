"""
시리즈 필터링 
    비교 연산자의 결과 시리즈를 사용하여 인덱싱 하면 조건을 만족하는 데이터만 필터링 가능
"""

from pandas import Series

s = Series(data = [100, 200, 300, 400, 500])
cond = s > 300
print(s[cond])
"""
3    400
4    500
dtype: int64
"""