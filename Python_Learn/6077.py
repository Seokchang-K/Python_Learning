a = int(input())

even = 0

for i in range(1, a+1):
    if i % 2 != 1:
        even = even + i

print(even)

# i 가 짝수일 경우 변수 even에 그 수를 더해서
# 1부터 주어진 정수까지의 수중 짝수를 모두 더해서 출력한다.