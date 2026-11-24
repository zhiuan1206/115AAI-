n = int(input())
original = n
count = 0

while n >= 10:
    total = 0

    for digit in str(n):
        total += int(digit)

    count += 1
    print("Pass", count, ":", total)
    n = total

print("Digital Root of", original, ":", n)