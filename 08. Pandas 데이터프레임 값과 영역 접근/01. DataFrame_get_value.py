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
특정 값 가져오기
    036360 종목의 현재가를 출력하기
        df.iloc[행번호, 열번호]
        df.loc[인덱스, 컬럼명]
"""

print(df.iloc[1, 1]) # 1790
print(df.loc["036360", "현재가"]) # 1790