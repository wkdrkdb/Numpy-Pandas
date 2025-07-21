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


# 대괄호[] 속성
print(s["월"]) # 100
print(s["수"]) # 300
print(s["화"]) # 200