shift = list(map(int, input().split()))
text = input()

result = ""
letter_count = 0
length = len(shift)

for ch in text:

    if 'a' <= ch <= 'z':
        j = letter_count % length
        new_ch = chr((ord(ch) - ord('a') - shift[j]) % 26 + ord('a'))
        result += new_ch
        letter_count += 1

    elif 'A' <= ch <= 'Z':
        j = letter_count % length
        new_ch = chr((ord(ch) - ord('A') - shift[j]) % 26 + ord('A'))
        result += new_ch
        letter_count += 1

    else:
        result += ch

print(result)