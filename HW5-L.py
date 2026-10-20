m = int(input())

count = 0
while m > 0:
    if m >= 50:
        m -= 50
    elif m >= 10:
        m -= 10
    elif m >= 5:
        m -= 5
    else:
        m -= 1
    count += 1

print(count)