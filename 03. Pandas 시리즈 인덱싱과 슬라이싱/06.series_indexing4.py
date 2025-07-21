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
# 연속적이지 않은 여러 개의 값을 한 번에 인덱싱


target = [0, 2]
print(s.iloc[target])
"""
월    100
수    300
dtype: int64
"""

target = ["월", "수"]
print(s.loc[target])
"""
월    100
수    300
dtype: int64
"""