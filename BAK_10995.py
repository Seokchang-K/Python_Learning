num = int(input())

for i in range(num):
    if i % 2 == 0:
        print('* ' * num)
    else:
        print(' *' * num)

# % 연산자는 나머지를 출력해준다.
# i % 2 가 0이 나오는 것은
# 0으로 딱 떨어지는 짝수 번째인 경우엔 한칸 붙어서 나온다.
# else i번 째가 1 3 5 7 9 처럼 홀수 번째일 경우를 한칸 떨어져서 나온다.
# ex) 0 번째는 붙어서, 1번째는 떨어져서, 2번째는 붙어서