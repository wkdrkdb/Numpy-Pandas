import pandas as pd

data = [100, 200, 300]
index = ["월", "화", "수"]
s = pd.Series(data, index)


"""
drop 메서드
    "원본은 유지"하고 값이 삭제된 시리즈 객체를 리턴
    s.drop("인덱스")
    s.drop(["인덱스1", "인덱스2"])
"""
s1 = s.drop("월")
print(s1)
"""
화    200   
수    300   
dtype: int64
"""
print(s)
"""
월    100   
화    200   
수    300   
dtype: int64
"""