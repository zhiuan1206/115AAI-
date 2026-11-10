def gcd(a, b):
    # 以 b = 0 為基底情況，遞迴輾轉相除法
    if b == 0:
        return a
    return gcd(b, a % b)

def simplify_recipe(tea, milk, syrup):
    # 找出三個數中所有非 0 數值的最大公因數
    g = 0
    for val in (tea, milk, syrup):
        if val > 0:
            if g == 0:
                g = val
            else:
                g = gcd(g, val)
                
    # 如果 g 為 0 或 1，代表沒有大於 1 的公因數，直接回傳原數值
    if g <= 1:
        return tea, milk, syrup
    else:
        return tea // g, milk // g, syrup // g

def main():
    import sys
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    idx = 1
    for _ in range(N):
        tea = int(input_data[idx])
        milk = int(input_data[idx+1])
        syrup = int(input_data[idx+2])
        idx += 3
        
        # 呼叫 simplify_recipe 取得最簡比例
        t, m, s = simplify_recipe(tea, milk, syrup)
        print(f"{t} {m} {s}")

if __name__ == '__main__':
    main()