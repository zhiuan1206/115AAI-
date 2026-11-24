n = int(input())
total = n
count = 0

while total >= 10:
    s = 0
    for digit in str(total):
        s += int(digit)
    count += 1
    total = s
    print(f"Pass {count} : {total}")

print(f"Digital Root of {n} : {total}")