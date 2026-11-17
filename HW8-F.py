
n = int(input())

# list：儲存所有輸入紀錄
records = []

# dict：每位使用者對應一個商品 set
user_items = {}

for _ in range(n):
    user, item = input().split()

    # tuple：儲存使用者與商品
    records.append((user, item))

    if user not in user_items:
        user_items[user] = set()

    # set：去除同一使用者的重複商品
    user_items[user].add(item)

# 輸入目標使用者與推薦數量
target, k = input().split()
k = int(k)

# 目標使用者買過的商品
target_items = user_items[target]

# dict：統計每個推薦商品的分數
scores = {}

# 找出相似使用者
for user in user_items:
    if user == target:
        continue

    # 至少有一個共同商品才算相似
    if user_items[user] & target_items:

        # 找出相似使用者買過，但目標沒買過的商品
        new_items = user_items[user] - target_items

        for item in new_items:
            if item not in scores:
                scores[item] = 0

            scores[item] += 1

# list：建立推薦排行榜
ranking = list(scores.items())

# 分數高的優先，同分依商品名稱字典序排列
ranking.sort(key=lambda x: (-x[1], x[0]))

# 取前 k 名
r = min(k, len(ranking))

if r == 0:
    print(0)
else:
    print(r)

    for item, score in ranking[:r]:
        print(item, score)
