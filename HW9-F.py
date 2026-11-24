a, b = map(int, input().split())

for num in range(a, b + 1):
    if num < 2:
        continue

    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")