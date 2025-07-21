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


# loc 속성: 시리즈 객체의 인덱스로 인덱싱
print(s.loc["월"]) # 100
print(s.loc["수"]) # 300
print(s.loc["화"]) # 200