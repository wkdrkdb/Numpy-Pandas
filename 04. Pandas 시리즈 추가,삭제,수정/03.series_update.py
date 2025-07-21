import pandas as pd

data = [100, 200, 300]
index = ["월", "화", "수"]
s = pd.Series(data, index)


# 시리즈의 행번호나 인덱스를 사용하여 value 수정 가능
s.iloc[0] = 1000
s.loc["수"] = 3000
print(s)
"""
월    1000  
화     200  
수    3000  
"""