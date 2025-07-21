"""
# python list에서는 데이터를 행 단위로 구성하는 경우 열 단위로 접근할 수가 없음
price = [
    [100, 80, 70, 90],
    [120, 110, 100, 110]
]
print(price[0]) # [100, 80, 70, 90]
"""

# ndarray로 2차원 데이터 표현하기
import numpy as np

price = [
    [100, 80, 70, 90],
    [120, 110, 100, 110]
]

arr = np.array(price)
print(arr[:, 0]) # [100 120]
print(arr[:, 1]) # [80 110]
