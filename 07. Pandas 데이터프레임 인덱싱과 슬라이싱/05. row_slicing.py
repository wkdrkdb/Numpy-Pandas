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
로우 슬라이싱
    iloc, loc 속성을 사용하여 슬라이싱
"""

print(df.iloc[0:2])
"""
           종가    PER   PBR
NAVER  157000  39.88  4.38
삼성전자    51300   8.52  1.45
"""

print(df.loc["NAVER": "삼성전자"])
"""
           종가    PER   PBR
NAVER  157000  39.88  4.38
삼성전자    51300   8.52  1.45
"""