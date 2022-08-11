a = int(input())

if a<0:
    if a%2 == 0:
        print('A')
    else:
        print('B')
else:
    if a%2 == 0:
        print('C')
    else:
        print('D')

# a가 음수인지 양수인지 확인 후에 홀짝을 구분해준다.