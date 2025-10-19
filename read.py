import pandas as pd

# 엑셀 파일 불러오기
df = pd.read_excel('stock.xlsx')

print(df.head())