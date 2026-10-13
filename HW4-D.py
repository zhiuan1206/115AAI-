h = int(input())

if h <= 2:
    total = h * 30
elif h <= 5:
    total = 60 + (h - 2) * 20
else:
    total = 120 + (h - 5) * 10

print(total)