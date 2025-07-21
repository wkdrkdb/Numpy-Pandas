from pandas import DataFrame

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]

index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]

df = DataFrame(data=data, index=index, columns=columns)
print(df)
"""
          종목명   현재가   등락률
037730     3R     1510     7.36
036360  3SOFT     1790     1.65
005760   ACTS     1185     1.28
"""


"""
특정 영역 가져오기
    데이터프레임에서 특정 영역 접근
        df.iloc[행번호 리스트, 열번호 리스트]
        df.loc[인덱스 리스트, 컬럼명 리스트]
"""

print(df.iloc[ [0, 1], [0, 1] ])
"""
          종목명   현재가
037730     3R      1510
036360    3SOFT    1790
"""

print(df.loc[ ["037730", "036360"], ["종목명", "현재가"] ])
"""
          종목명   현재가
037730     3R      1510
036360    3SOFT    1790   
"""