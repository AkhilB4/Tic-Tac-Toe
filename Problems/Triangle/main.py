n = int(input())
k = n - 1
for i in range(n):
    for _ in range(k):
        print(" ", end="")
    k -= 1
    for _ in range(2 * i + 1):
        print("#", end="")
    print()
