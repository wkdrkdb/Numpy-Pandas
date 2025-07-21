import pandas as pd

arr = [0, 1, 2, 3]
print(type(arr)) # list

s = pd.Series(arr)
print(s)
"""
0    0
1    1
2    2
3    3
"""

print(type(s)) # Series