# 第一行讀取 x1, y1
x1, y1 = map(int, input().split())

# 第二行讀取 x2, y2
x2, y2 = map(int, input().split())

# 計算距離平方
dist_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2

print(dist_sq)