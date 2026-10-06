N = int(input())

# 拆解各位數
a = N // 100         # 百位數
b = (N // 10) % 10   # 十位數
c = N % 10           # 個位數

# 計算總和與乘積
sum_val = a + b + c
prod_val = a * b * c

# 計算反轉後的數字（個位數變百位、十位不變、百位數變個位）
reversed_val = c * 100 + b * 10 + a

# 依序輸出 4 行
print(f"{a} {b} {c}")
print(sum_val)
print(prod_val)
print(reversed_val)