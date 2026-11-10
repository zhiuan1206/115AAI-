def best_total(prices, index, remaining):
    # 遞迴終止條件：若已考慮完所有商品，則沒有額外花費
    if index == len(prices):
        return 0
    
    # 分支 1：不選目前商品，直接考慮下一個商品
    skip_cost = best_total(prices, index + 1, remaining)
    
    # 分支 2：若買得起目前商品，則可選擇購買
    take_cost = 0
    if prices[index] <= remaining:
        take_cost = prices[index] + best_total(prices, index + 1, remaining - prices[index])
        
    # 回傳兩種選擇中的最大花費金額
    return max(skip_cost, take_cost)

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    B = int(input_data[1])
    
    # 讀取 N 個商品的價格（保持原本順序，不排序、不刪除重複）
    prices = []
    for i in range(2, 2 + N):
        prices.append(int(input_data[i]))
        
    # 主程式呼叫 best_total(prices, 0, B)
    ans = best_total(prices, 0, B)
    print(ans)

if __name__ == '__main__':
    main()