# 1. 讀取菜單資料
M = int(input())
menu_names = []
menu_prices = []
menu_total_qty = []

for _ in range(M):
    name, price = input().split()
    menu_names.append(name)
    menu_prices.append(int(price))
    menu_total_qty.append(0)  # 預設總杯數為 0

# 2. 讀取訂單資料並使用平行串列記錄學生
N = int(input())
student_names = []
student_orders = []  # 存每位學生的訂單列表：[(drink_index, qty), ...]

for _ in range(N):
    s_name, d_name, qty_str = input().split()
    qty = int(qty_str)
    
    # 找到飲料在菜單中的索引
    d_idx = menu_names.index(d_name)
    menu_total_qty[d_idx] += qty
    
    # 檢查學生是否已記錄過，若未記錄則加入
    if s_name not in student_names:
        student_names.append(s_name)
        student_orders.append([])
    
    s_idx = student_names.index(s_name)
    student_orders[s_idx].append((d_idx, qty))

# 3. 計算每種飲料折減後的實際單價
actual_prices = []
for i in range(M):
    if menu_total_qty[i] >= 10:
        actual_prices.append(menu_prices[i] - 5)
    else:
        actual_prices.append(menu_prices[i])

# 4. 輸出飲料統計結果（依菜單順序）
for i in range(M):
    print(f"DRINK {menu_names[i]} {menu_total_qty[i]}")

# 5. 計算並輸出每位學生的應付金額（依首次出現順序）
grand_total = 0
for i in range(len(student_names)):
    s_total = 0
    for d_idx, qty in student_orders[i]:
        s_total += actual_prices[d_idx] * qty
    grand_total += s_total
    print(f"STUDENT {student_names[i]} {s_total}")

# 6. 輸出全班總額
print(f"TOTAL {grand_total}")