B, N, R, C = map(int, input().split())

# 1. 計算服務費（無條件捨去至整數）
service_fee = (B * R) // 100

# 2. 計算應付總額 T
total = B + service_fee - C
if total < 0:
    total = 0

# 3. 計算分攤金額與人數
q = total // N
r = total % N

b = r
a = N - b

# 輸出結果
print(total)
print(f"{q} {a}")
print(f"{q + 1} {b}")