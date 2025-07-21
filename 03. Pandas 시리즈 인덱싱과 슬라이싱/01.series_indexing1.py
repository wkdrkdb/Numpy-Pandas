import pandas as pd

data = [100, 200, 300]
index = ["월", "화", "수"]
s = pd.Series(data, index)
print(s)
"""
월    100
화    200
수    300
dtype: int64
"""


# iloc 속성: 시리즈 객체의 행번호를 사용하여 인덱싱
print(s.iloc[0]) # 100
print(s.iloc[2]) # 300
print(s.iloc[-1]) # 300