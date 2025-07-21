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
print(s.index) # Index(['월', '화', '수'], dtype='object')
print(s.values) # [100 200 300]
print(s.array) 
"""
<NumpyExtensionArray>
[np.int64(100), np.int64(200), np.int64(300)]
Length: 3, dtype: int64
"""