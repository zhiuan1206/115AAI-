# 讀取第 1 行 a, b 與第 2 行 c, d
a, b = map(int, input().split())
c, d = map(int, input().split())

# 計算行列式
det = a * d - b * c

# 計算反矩陣元素
r11 = d / det
r12 = -b / det
r21 = -c / det
r22 = a / det

# 輸出保留小數點後 4 位
print(f"{r11:.4f} {r12:.4f}")
print(f"{r21:.4f} {r22:.4f}")