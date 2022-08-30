# plate = [[0 for _ in range(19)] for _ in range(19)]
# 이렇게 코드를 짜도 되고

plate=[]

for i in range(20):
    plate.append([])
    for _ in range(20):
        plate[i].append(0)

# 이렇게 해서 해도 된다.

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    plate[a-1][b-1] = 1
    # 인덱싱의 시작은 0부터 이기에 1,1 의 좌표는 인덱싱으로 치면 0,0이다.

for i in range(19):
    for j in range(19):
        print(plate[i][j], end=' ')
    print()
    # 이부분의 print를 안해주면 끝까지 공백으로 끝나는 print를 쭉 이어서 한다.
    # 바둑판식 배열을 위해 print를 해줘야 한다.