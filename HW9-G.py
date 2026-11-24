shift = list(map(int, input().split()))
text = input()

result = ""
length = len(shift)

for i in range(len(text)):
    ch = text[i]

    if 'a' <= ch <= 'z':
        j = i % length
        new_ch = chr((ord(ch) - ord('a') - shift[j]) % 26 + ord('a'))
        result += new_ch

    elif 'A' <= ch <= 'Z':
        j = i % length
        new_ch = chr((ord(ch) - ord('A') - shift[j]) % 26 + ord('A'))
        result += new_ch

    else:
        result += ch

print(result)