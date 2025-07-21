"""
2차원 표에서 로우 단위로 데이터를 딕셔너리로 표현
"""

from pandas import DataFrame

data = [
    {"종가": 157000, "PER": 39.88, "PBR": 4.38},
    {"종가": 51300, "PER": 8.52, "PBR": 1.45},
    {"종가": 68800, "PER": 10.03, "PBR": 0.87},
    {"종가": 140000, "PER": 228.38, "PBR": 2.16}
]

index = ["NAVER", "삼성전자", "LG전자", "카카오"]
df = DataFrame(data=data, index=index)
print(df)
"""
         종가     PER   PBR  
NAVER  157000   39.88  4.38    
삼성전자    51300    8.52  1.45
LG전자    68800   10.03  0.87  
카카오    140000  228.38  2.16 
"""