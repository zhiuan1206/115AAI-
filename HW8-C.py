
n, m = map(int, input().split())

# 讀取兩個社團名單，轉換成 set 去除重複
A = set(input().split())
B = set(input().split())

# 1. 交集：兩個社團都有的成員
result1 = A & B

# 2. 聯集：至少參加一個社團的成員
result2 = A | B

# 3. 差集：只參加 A 社團的成員
result3 = A - B

# 4. 差集：只參加 B 社團的成員
result4 = B - A

# 輸出結果
for result in [result1, result2, result3, result4]:
    if len(result) == 0:
        print("NONE")
    else:
        print(" ".join(sorted(result)))
