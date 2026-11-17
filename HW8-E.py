
n = int(input())

# set：儲存不重複的 (學生, 攤位) 組合
records = set()

for _ in range(n):
    student, booth = input().split()
    records.add((student, booth))

# dict：統計每位學生獲得的不同攤位章數
count = {}

for student, booth in records:
    if student not in count:
        count[student] = 0
    count[student] += 1

# list：建立排行榜
ranking = list(count.items())

# 章數多的在前，章數相同則姓名字典序小的在前
ranking.sort(key=lambda x: (-x[1], x[0]))

# 輸出不重複的有效紀錄數
print(len(records))

# 輸出排行榜
for student, total in ranking:
    print(student, total)
