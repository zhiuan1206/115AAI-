n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # >4 表示欄寬為 4 且靠右對齊
        print(f"{i * j:>4}", end="")
    print()  # 每列結束後換行