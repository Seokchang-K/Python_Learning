# 먼저 빈 미로를 만들어 준다.
maze = [[0 for _ in range(10)]for _ in range(10)]

# 빈 미로에 주어진 미로를 채워 넣는다.
for i in range(10):
    maze[i] = list(map(int,input().split()))

# 시작값의 좌표를 정해준다.
x = 1
y = 1

while True:
    if maze[x][y] == 0:
        maze[x][y] = 9
    # 만약 해당 위치가 빈 공간이라면 지나갔단 표시로 9를 기입한다.
    elif maze[x][y] == 2:
        maze[x][y] = 9
        break
    # 만약 해당 위치가 먹이가 있는 2번이라면 지나갔단 표시로 9를 남기고 미로를 탈출한다.

    if maze[x][y+1] == 1 and maze[x+1][y] == 1:
        break
    # 만약 미로가 오른쪽으로 가도 밑으로 가도 막혀 있다면 게임오버

    if maze[x][y+1] != 1:
        y = y + 1
    # 만약 미로의 오른쪽 방향이 막히지 않았다면 미로의 오른쪽으로 이동
    elif maze[x+1][y] != 1:
        x = x + 1
    # 만약 미로의 밑의 방향이 막히지 않았다면 미로의 밑으로 이동
        
# 미로 탐색이 끝나게 되면 개미가 움직인 미로를 보여준다.
for i in range(10):
    for j in range(10):
        print(maze[i][j], end=' ')
    print()