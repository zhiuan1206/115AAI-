import sys

# 讀取整行輸入（包含頭尾空白與換行符號）
line = sys.stdin.readline()
if line.endswith('\n'):
    line = line[:-1]
if line.endswith('\r'):
    line = line[:-1]

# 1. 移除頭尾空白並轉小寫
trimmed = line.strip().lower()

# 2. 將中間連續空白替換為單一底線
if trimmed:
    # split() 預設會自動處理任意長度的連續空白
    formatted_username = "_".join(trimmed.split())
else:
    formatted_username = ""

# 3. 輸出整理後的結果
print(formatted_username)

# 4. 檢查合法性
is_valid = True

# 檢查長度是否在 6 至 16 之間
if not (6 <= len(formatted_username) <= 16):
    is_valid = False
else:
    # 檢查每個字元是否為小寫字母、數字或底線
    for ch in formatted_username:
        if not (ch.islower() or ch.isdigit() or ch == '_'):
            is_valid = False
            break

if is_valid:
    print("VALID")
else:
    print("INVALID")