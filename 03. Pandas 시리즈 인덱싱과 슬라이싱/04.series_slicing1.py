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


# 행번호를 사용하여 슬라이싱: iloc[시작 행번호: 끝 행번호]
print(s.iloc[0:2])
"""
월    100
화    200
dtype: int64
"""
