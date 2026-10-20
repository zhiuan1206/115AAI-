a, b, k = map(int, input().split())

count = 0
total_sum = 0

# 遍歷區間 [a, b] 內的每個數字
for i in range(a, b + 1):
    if i % k == 0:
        count += 1
        total_sum += i

print(f"{count} {total_sum}")