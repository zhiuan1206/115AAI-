
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def simplify_recipe(tea, milk, syrup):
    g = gcd(gcd(tea, milk), syrup)

    return tea // g, milk // g, syrup // g


N = int(input())

for _ in range(N):
    tea, milk, syrup = map(int, input().split())

    a, b, c = simplify_recipe(tea, milk, syrup)

    print(a, b, c)
