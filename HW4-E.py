a, b, c = map(int, input().split())

# 計算判別式 D = b^2 - 4ac
D = b * b - 4 * a * c

if D > 0:
    print(2)
elif D == 0:
    print(1)
else:
    print(0)