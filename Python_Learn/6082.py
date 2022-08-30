a = int(input())

for i in range(1, a+1):
    if i%10==3 or i%10==6 or i%10==9:
        print('X', end=' ')
 
    else:
        print(i, end=' ')

# if 문에 or을 쓰려면 식을 각자 다 써주고 사이사이에 or을 넣으면 된다.