def parking_fee(minutes):
    # 停車 0 分鐘不收費
    if minutes == 0:
        return 0
    
    # 計算需要的 30 分鐘區間數（不足 30 分鐘也算一個區間，可用向上取整或整數除法）
    # (minutes + 29) // 30 相當於將分鐘數無條件進位到下一個 30 的倍數再除以 30
    intervals = (minutes + 29) // 30
    fee = intervals * 30
    
    # 單次停車費最高上限為 200 元
    if fee > 200:
        fee = 200
        
    return fee

def main():
    # 讀取第一行的紀錄數 N
    N = int(input())
    # 讀取第二行的 N 個整數，代表各車停車分鐘數
    minutes_list = list(map(int, input().split()))
    
    # 計算每台車的費用
    fees = []
    for m in minutes_list:
        fees.append(parking_fee(m))
        
    # 第一行輸出 N 個費用，以一個空白分隔
    print(" ".join(map(str, fees)))
    
    # 第二行輸出所有費用的總和
    print(sum(fees))

if __name__ == '__main__':
    main()