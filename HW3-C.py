x1, x2, x3 = map(int, input().split())

# 計算平均數與母體變異數
m = (x1 + x2 + x3) / 3
v = ((x1 - m)**2 + (x2 - m)**2 + (x3 - m)**2) / 3

# 輸出保留兩位小數
print(f"{m:.2f}")
print(f"{v:.2f}")