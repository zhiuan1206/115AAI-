N = int(input())

names = []
subtotals = []

max_subtotal = -1
top_product = ""

for _ in range(N):
    parts = input().split()
    name = parts[0]
    price = int(parts[1])
    quantity = int(parts[2])

    # 計算需付費件數：每 3 件付 2 件費用
    paid_quantity = (quantity // 3) * 2 + (quantity % 3)
    subtotal = paid_quantity * price

    names.append(name)
    subtotals.append(subtotal)

    # 紀錄最高小計商品（同額選較早輸入者，故僅使用 >）
    if subtotal > max_subtotal:
        max_subtotal = subtotal
        top_product = name

# 計算初步總金額與滿額折抵
total_sum = sum(subtotals)
if total_sum >= 1000:
    final_total = total_sum - 100
else:
    final_total = total_sum

# 輸出 N 行商品名稱與小計
for i in range(N):
    print(f"{names[i]} {subtotals[i]}")

# 輸出 TOTAL 金額與 TOP 商品
print(f"TOTAL {final_total}")
print(f"TOP {top_product}")