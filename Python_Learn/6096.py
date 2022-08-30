plate = [[0 for _ in range(19)] for _ in range(19)]

# 먼저 0으로 이루어진 게임 판을 만든다.

for i in range(19):
    plate[i] = list(map(int, input().split()))
    
# 그 판을 한줄 한줄 들어온 판으로 교체한다.

n_flip = int(input())

# 뒤집는 횟수를 가져온다.

for i in range(n_flip):
    x, y = map(int, input().split())
    x = x-1
    y = y-1

    for j in range(19):
        if plate[x][j] == 0:
            plate[x][j] = 1
        else:
            plate[x][j] = 0
        # plate 의 [x] 번째 리스트의 j번 수가 0이라면 이를 1로 바꾸고
        # 아니면 0으로 바꿔줘라

        if plate[j][y] == 0:
            plate[j][y] = 1
        else:
            plate[j][y] = 0
        # plate의 [j] 번째 리스트의 y번 수가 0이라면 1로 바꾸고
        # 아니면 0으로 바꿔라

for i in range(19):
    for j in range(19):
        print(plate[i][j], end=' ')
        # plate 리스트에서 [i]번째 리스트 중 j 번 숫자를 print 해줘라
        # 그리고 이를 19번 반복해 한줄이 나온다.(세로로 19줄)
    print()
    # 위의 print를 통해서 위에서 반복해 나온 한줄을 출력해준다.
    # 19번 반복해서 가로로 19줄 출력