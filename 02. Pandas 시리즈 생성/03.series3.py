import pandas as pd

data = [500, 800, 200]
index = ["메로나", "누가바", "빠삐코"]
s = pd.Series(data, index)
print(s)
"""
메로나    500
누가바    800
빠삐코    200
dtype: int64
"""