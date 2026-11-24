n = int(input())
original = n
count = 1

while True:
    total = 0

    for digit in str(n):
        total += int(digit)

    print("Pass", count, ":", total)

    if total < 10:
        break

    n = total
    count += 1

print("Digital Root of", original, ":", total)