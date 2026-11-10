def normalize(text):
    # 只保留 ASCII 英文字母與數字，並轉為小寫
    result = ""
    for char in text:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
            # 若是大寫字母則轉成小寫
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char
    return result

def is_palindrome(text, left, right):
    # 遞迴終止條件：當左右索引交錯或重疊，代表檢查完畢，為回文
    if left >= right:
        return True
    # 若兩端字元不相符，則不是回文
    if text[left] != text[right]:
        return False
    # 縮小範圍，往內遞迴檢查
    return is_palindrome(text, left + 1, right - 1)

def main():
    import sys
    # 讀取一整行原始密語（可能包含空白或符號）
    line = sys.stdin.readline()
    if not line:
        return
    # 去除結尾的換行字元
    raw_text = line.rstrip('\r\n')
    
    clean_text = normalize(raw_text)
    
    # 判斷是否為回文
    if len(clean_text) <= 1:
        print("YES")
    else:
        if is_palindrome(clean_text, 0, len(clean_text) - 1):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()