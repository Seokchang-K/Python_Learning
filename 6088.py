a, d, n = map(int, input().split())

for i in range(a, n+1):
    i = i + d
    if i == n:
        print(i)

