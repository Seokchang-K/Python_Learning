r, g, b = map(int, input().split())

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)

print(r*g*b)

# 이건 잘 모르겠다.

# for문을 돌면서 처음 
# i가 0이면서 j가 0이고  k가 0인 경우 -> 000
# i가 0이면서 j가 0이고  k가 1인 경우 -> 001
# i가 0이면서 j가 1이고  k가 0인 경우 -> 010
# i가 0이면서 j가 1이고  k가 1인 경우 -> 011
# i가 1이면서 j가 0이고  k가 0인 경우 -> 100
# i가 1이면서 j가 0이고  k가 1인 경우 -> 101
# i가 1이면서 j가 1이고  k가 0인 경우 -> 110
# i가 1이면서 j가 1이고  k가 1인 경우 -> 111