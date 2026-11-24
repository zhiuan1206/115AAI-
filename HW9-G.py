cipher = input().split()
text = input()

result = ""

for i in range(len(text)):
    if text[i].isalpha():
        shift = int(cipher[i % len(cipher)])

        if text[i].isupper():
            result += chr((ord(text[i]) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += chr((ord(text[i]) - ord('a') - shift) % 26 + ord('a'))
    else:
        result += text[i]

print(result)