# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall

a = int(input())

if 3<=a<=5:
    print('spring')
else:
    if 6<= a <=8:
        print('summer')
    else:
        if 9<= a <=11:
            print('fall')
        else:
            print('winter')