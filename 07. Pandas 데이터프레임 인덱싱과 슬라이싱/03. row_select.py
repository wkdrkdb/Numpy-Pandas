from pandas import DataFrame

data = [
    [157000, 39.88, 4.38],
    [51300, 8.52, 1.45],    
    [68800, 10.03, 0.87],
    [140000, 228.38, 2.16]
]

index = ["NAVER", "삼성전자", "LG전자", "카카오"]
columns = ["종가", "PER", "PBR"]
df = DataFrame(data=data, index=index, columns=columns)
print(df)
"""
           종가     PER   PBR  
NAVER  157000   39.88  4.38    
삼성전자    51300    8.52  1.45
LG전자    68800   10.03  0.87  
카카오    140000  228.38  2.16 
"""


"""
로우(row) 선택
    데이터프레임에서 로우(row)를 선택할 때는 iloc나 loc 속성을 사용
        loc속성: 인덱스를 사용해서 로우를 선택
        iloc속성: 행번호를 사용해서 로우를 선택
"""

print(df.iloc[1])
"""
종가     51300.00
PER        8.52
PBR        1.45
Name: 삼성전자, dtype: float64
"""

print(df.loc["삼성전자"])
"""
종가     51300.00
PER        8.52
PBR        1.45
Name: 삼성전자, dtype: float64
"""