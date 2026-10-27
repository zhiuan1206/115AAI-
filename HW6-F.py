import sys

# 讀取移動位置數 K
K = int(sys.stdin.readline())

# 完整讀取第二行原始訊息 S (保留頭尾與中間的所有空白)
S = sys.stdin.readline()
if S.endswith('\n'):
    S = S[:-1]
if S.endswith('\r'):
    S = S[:-1]

result = []
for ch in S:
    if 'A' <= ch <= 'Z':
        # 大寫字母轉換
        new_ch = chr((ord(ch) - ord('A') + K) % 26 + ord('A'))
        result.append(new_ch)
    elif 'a' <= ch <= 'z':
        # 小寫字母轉換
        new_ch = chr((ord(ch) - ord('a') + K) % 26 + ord('a'))
        result.append(new_ch)
    else:
        # 非英文字母維持原樣
        result.append(ch)

print("".join(result))