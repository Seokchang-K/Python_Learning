# 평가 기준
# 점수 범위   : 평가
#  90 ~ 100  : A
#  70 ~   89 : B
#  40 ~   69 : C
#   0 ~   39 : D
# 로 평가되어야 한다.

a = int(input())

if a>=90:
    print('A')
else:
    if a>=70:
        print('B')
    else:
        if a>=40:
            print('C')
        else:
            print('D')
