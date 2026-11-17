
n = int(input())
stock = {}

# 輸入初始商品庫存
for _ in range(n):
    name, qty = input().split()
    stock[name] = int(qty)

q = int(input())

total = 0       # 成功賣出的商品總數
failed = 0      # 被拒絕的購買次數

for _ in range(q):
    op, name, qty = input().split()
    qty = int(qty)

    if op == "ADD":
        # 商品不存在就新增，存在就增加庫存
        if name not in stock:
            stock[name] = 0
        stock[name] += qty

    elif op == "BUY":
        # 商品存在且庫存足夠才能購買
        if name in stock and stock[name] >= qty:
            stock[name] -= qty
            total += qty
        else:
            failed += 1

# 輸出統計結果
print(total, failed)

# 商品名稱依字母順序輸出
for name in sorted(stock):
    print(name, stock[name])
