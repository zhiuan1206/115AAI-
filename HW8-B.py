
n = int(input())

runners = []

# 讀取跑者資料
for i in range(n):
    name, time, penalty = input().split()

    time = int(time)
    penalty = int(penalty)

    # 使用 tuple 儲存資料
    runners.append((name, time, penalty))

# 依照總秒數、原始秒數、姓名排序
runners = sorted(runners, key=lambda x: (x[1] + x[2], x[1], x[0]))

# 輸出結果
for runner in runners:
    name = runner[0]
    total = runner[1] + runner[2]

    print(name, total)
