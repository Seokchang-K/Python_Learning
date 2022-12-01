n = int(input())
line = list(map(int, input().split()))
outcome = []

for i in range(n):
    outcome.insert(i-line[i], i+1)

for k in outcome:
    print(k, end=' ')