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


# 인덱스를 기반으로 슬라이싱: loc[시작 인덱스: 끝 인덱스] (끝 인덱스를 포함함)
print(s.loc["월": "수"])
"""
월    100
화    200
수    300
dtype: int64
"""
