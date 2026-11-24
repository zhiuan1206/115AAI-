a, b = map(int, input().split())

start = min(a, b)
end = max(a, b)

result = []

for num in range(start, end + 1):
    if num > 1:
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            result.append(num)

print(*result)