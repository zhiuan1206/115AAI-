
def count_ways(step, n, blocked, memo):
    # 超過終點，代表此走法無效
    if step > n:
        return 0

    # 踩到損壞階梯，走法無效
    if blocked[step]:
        return 0

    # 抵達終點
    if step == n:
        return 1

    # 已經計算過，直接回傳
    if memo[step] != -1:
        return memo[step]

    # 分別嘗試走 1 階和 2 階
    memo[step] = (
        count_ways(step + 1, n, blocked, memo)
        + count_ways(step + 2, n, blocked, memo)
    )

    return memo[step]


# 主程式
data = list(map(int, input().split()))
n, k = data

blocked = [False] * (n + 1)

if k > 0:
    damaged = list(map(int, input().split()))
    for x in damaged:
        blocked[x] = True

memo = [-1] * (n + 1)

print(count_ways(0, n, blocked, memo))
