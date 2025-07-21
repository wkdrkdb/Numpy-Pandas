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
멀티 컬럼 선택
    컬럼을 리스트로 구성한 후 인덱싱 기호에 리스트를 전달
    df[["컬럼명1", "컬럼명2"]]
"""

print(df[ ["PER", "PBR"] ])
"""
          PER   PBR    
NAVER   39.88  4.38    
삼성전자     8.52  1.45
LG전자    10.03  0.87  
카카오    228.38  2.16 
"""