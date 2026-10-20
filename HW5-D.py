n = int(input())
scores = list(map(int, input().split()))

total = 0
passed_count = 0

for score in scores:
    total += score
    if score >= 60:
        passed_count += 1

avg = total / n

print(f"{avg:.2f}")
print(passed_count)