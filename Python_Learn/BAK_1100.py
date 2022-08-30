# 문제
# 체스판은 8×8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 가장 왼쪽 위칸 (0,0)은 하얀색이다. 
# 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄부터 8개의 줄에 체스판의 상태가 주어진다. ‘.’은 빈 칸이고, ‘F’는 위에 말이 있는 칸이다.

board = [list(input()) for _ in range(8)]
# - 0 1 2 3 4 5 6 7
# 0 w b w b w b w b
# 1 b w b w b w b w
# 2 w b w b w b w b 
# 3 b w b w b w b w
# 4 w b w b w b w b
# 5 b w b w b w b w
# 6 w b w b w b w b
# 짝수 열에는 짝수에만 w 가 있고.
# 홀수 열에는 홀수에만 w 가 있다.

total = 0

for i in range(8):
    for j in range(8):
        if i%2 == j%2 and board[i][j] == 'F':
            # 짝수행에 짝수 열이고 or 홀수 행에 홀수 열이고
            # 해당 좌표에 말이 서있다면
            # total에 1을 더해 준다.
            total += 1

print(total)