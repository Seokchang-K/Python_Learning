a, b = map(int, input().split())

a = bool(a)
b = bool(b)

# print((not a and not b) or (a and b))

if a == b:
    print(True)
else :
    print(False)