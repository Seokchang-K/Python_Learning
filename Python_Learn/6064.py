a, b, c = map(int, input().split())

d = 0

if a > b:
    d = b
else:
    d = a

e = 0

if d > c:
    e = c
else:
    e = d

print(e)