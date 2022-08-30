# 문제
# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 
# 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 
# 색종이의 변과 도화지의 변이 평행하도록 붙인다. 
# 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.

paper = [[0 for _ in range(100)] for _ in range(100)]
# 빈 흰색 도화지를 만든다

num_paper = int(input())

color_paper = []

for _ in range(num_paper):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            # 색종이는 10 x 10 의 정사각형이기에 x, x+10 의 범위를 검게 칠한다.
            paper[i][j] = 1

total = 0

for i in paper:
    total += sum(i)
    # paper 2차원 리스트에서 하위 리스트 하나씩 총 합을 구해
    # 색종이가 붙은 검은 영역을 구한다.

print(total)