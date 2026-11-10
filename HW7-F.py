
def best_total(prices, index, remaining):
    # 所有商品都考慮完畢
    if index == len(prices):
        return 0

    # 情況一：不購買目前商品
    not_buy = best_total(prices, index + 1, remaining)

    # 情況二：購買目前商品
    buy = 0
    if prices[index] <= remaining:
        buy = prices[index] + best_total(
            prices, index + 1, remaining - prices[index]
        )

    # 回傳兩種情況中較大的總金額
    return max(not_buy, buy)


# 主程式
N, B = map(int, input().split())
prices = list(map(int, input().split()))

print(best_total(prices, 0, B))
