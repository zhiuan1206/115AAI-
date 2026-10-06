# 讀取矩陣 A (第 1、2 行)
a, b = map(int, input().split())
c, d = map(int, input().split())

# 讀取矩陣 B (第 3、4 行)
e, f = map(int, input().split())
g, h = map(int, input().split())

# 計算矩陣乘積 C 的元素
c11 = a * e + b * g
c12 = a * f + b * h
c21 = c * e + d * g
c22 = c * f + d * h

# 輸出 2 行，每行包含 2 個數字以空白隔開
print(f"{c11} {c12}")
print(f"{c21} {c22}")