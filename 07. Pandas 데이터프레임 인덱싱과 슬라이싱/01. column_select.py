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
컬럼 선택
    대괄호["컬럼명"]을 통해서 단일 컬럼 선택 가능
        df["종가"]
        컬럼을 표현하는 시리즈 타입의 객체
        index 는 회사 이름
        value 는 종가
"""

print(df["종가"])
"""
NAVER    157000
삼성전자      51300      
LG전자      68800        
카카오      140000       
Name: 종가, dtype: int64 
"""

print(df["PER"])
"""
NAVER     39.88
삼성전자       8.52
LG전자      10.03
카카오      228.38
Name: PER, dtype: float64
"""