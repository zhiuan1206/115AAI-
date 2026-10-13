# 讀取三個邊長並進行排序
sides = sorted(map(int, input().split()))
a, b, c = sides[0], sides[1], sides[2]

# 判斷是否能組成三角形
if a + b <= c:
    print("Invalid")
else:
    # 進行分類
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")