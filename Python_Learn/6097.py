# 판떼기 크기 가져오기
a, b = map(int,input().split())

# 판떼기 만들어 주기
game = [[0 for _ in range(b)]for _ in range(a)]

# 막대기 갯수 가져오기
st = int(input())

for _ in range(st):
    l, d, x, y = map(int,input().split())
    x = x-1
    y = y-1
    # 막대 길이 방향 좌표 가져오기
    # 우리는 0번부터 만들었으니까 -1 해줘야 한다.

    for j in range(l):
        if d == 0:
            game[x][y+j] = 1
            # 만약에 방향이 0이면 가로니까
            # y에 j를 더해가며 한다.
        else:
            game[x+j][y] = 1
            # 만약에 방향이 1이면 세로방향이니
            # x에 j를 더해가며 바꾼다.

for i in range(a):
    for j in range(b):
        print(game[i][j], end=' ')
    print()