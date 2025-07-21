import pandas as pd

data = [100, 200, 300]
index = ["월", "화", "수"]
s = pd.Series(data, index)


# 딕셔너리와 유사한 방식으로 값 추가 가능 
# s.loc[인덱스] = 값
s.loc["목"] = 400
print(s)
"""
월    100   
화    200   
수    300   
목    400   
dtype: int64"""