def is_prime(n):
    # 質數是大於 1 且正因數只有 1 與自己的整數
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # 試除法：只需檢查至除數平方不大於 n 的範圍 (步進為 6 可優化，或直接用 range 檢查)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    # 讀取輸入的 L 與 R
    L, R = map(int, input().split())
    
    primes = []
    # 在主程式對區間內每個整數呼叫 is_prime(n)
    for num in range(L, R + 1):
        if is_prime(num):
            primes.append(num)
            
    # 輸出結果
    if len(primes) == 0:
        print("NONE")
        print("0 0")
    else:
        print(" ".join(map(str, primes)))
        print(f"{len(primes)} {sum(primes)}")

if __name__ == '__main__':
    main()