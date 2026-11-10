def count_ways(step, n, blocked, memo):
    # 超過目標階梯，走法為 0
    if step > n:
        return 0
    # 若當前階梯是損壞的，不能落在此處，走法為 0
    if blocked[step]:
        return 0
    # 剛好到達第 n 階，找到一種走法
    if step == n:
        return 1
    
    # 若 memo 中已經算過此狀態，直接回傳（記憶化搜尋）
    if memo[step] != -1:
        return memo[step]
    
    # 遞迴分別處理再走 1 階與 2 階（函數內不使用迴圈或推導式）
    ways = count_ways(step + 1, n, blocked, memo) + count_ways(step + 2, n, blocked, memo)
    
    # 儲存計算結果至 memo
    memo[step] = ways
    return ways

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1]) if len(input_data) > 1 else 0
    
    # 建立 blocked 串列（長度 N + 1，初值皆為 False）
    blocked = [False] * (N + 1)
    
    # 讀取 K 個損壞階梯編號並標記
    idx = 2
    for _ in range(K):
        broken_step = int(input_data[idx])
        blocked[broken_step] = True
        idx += 1
        
    # 初始化 memo 串列（長度 N + 1，初值皆為 -1）
    memo = [-1] * (N + 1)
    
    # 從地面的第 0 階出發
    ans = count_ways(0, N, blocked, memo)
    print(ans)

if __name__ == '__main__':
    main()