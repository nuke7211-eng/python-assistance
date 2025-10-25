
f = 0

try:
        
    f = open("stock.csv", "rt", encoding="utf-8")

    while True:
        r = f.readline()
        if not r:
                break
        print(r)

except FileNotFoundError:
    print('파일이 없습니다.')
finally:
    if f:
        f.close()
    print('파일을 닫았습니다.')

