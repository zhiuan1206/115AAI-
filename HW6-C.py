# 讀取每日目標 G 與 7 天步數
G = int(input())
steps = list(map(int, input().split()))

# 1. 總步數
total_steps = sum(steps)

# 2. 達標天數與最長連續達標天數計算
target_count = 0
max_streak = 0
current_streak = 0

for step in steps:
    if step >= G:
        target_count += 1
        current_streak += 1
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        current_streak = 0

# 3. 找出最高步數發生的所有日期 (1-based)
max_val = max(steps)
max_days = []
for i in range(7):
    if steps[i] == max_val:
        max_days.append(str(i + 1))

# 輸出結果 (共四行)
print(total_steps)
print(target_count)
print(" ".join(max_days))
print(max_streak)