a, b, c = map(int, input().split())

# 先假設 a 為最大值
max_val = a

# 依序用條件判斷比較 b 與 c
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c

print(max_val)