"""
# python list에 있는 값에 10 곱하기
data = [1, 2, 3, 4]
result = []

for i in data:
    result.append(i * 10)

print(result)
"""

import numpy as np
data = [1, 2, 3, 4]
print(type(data)) # list
arr = np.array(data) 
print(type(arr)) # ndarray
arr10 = arr * 10 
print(arr10) # [10 20 30 40]