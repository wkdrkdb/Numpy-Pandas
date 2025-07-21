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
멀티 로우 선택
    리스트로 행번호 또는 인덱스를 표현하고 이를 iloc나 loc 속성에 사용
        df.iloc[[0, 1]]
        df.loc[["인덱스1", "인덱스2"]]
"""

print(df.iloc[ [0, 2] ])
"""
           종가    PER   PBR
NAVER  157000  39.88  4.38
LG전자    68800  10.03  0.87
"""

print(df.loc[ ["NAVER", "LG전자"] ])
"""
           종가    PER   PBR
NAVER  157000  39.88  4.38
LG전자    68800  10.03  0.87
"""