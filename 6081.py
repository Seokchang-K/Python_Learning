a = int(input(), 16)

for i in range(1, 16):
    print('%X'%a, '*%X'%i, '=%X'%(a*i), sep='')
    # print('%X*%X=%X' % (a, i, a*i))

# print('%X'%n)   
# #n에 저장되어있는 값을 16진수(hexadecimal) 형태로 출력
# int의 인자에 16을 넣어서 16진수로 받아온다.
# for문의 range 에 1~16까지 넣어 16번 반복한다.
# print 로 16진수로 표현된('%X'%a) a, 그 뒤에 *와 16진수로 표현된 i를 출력('*%X'%i)
# 맨마지막으론 = 과 16진수로 표현된 a*i 를 출력한다.('=%X'%(a*i))
# print의 인자로 sep=''을 넣어서 각 문자 사이 공간을 없앤다.(디폴트는 공백-space)