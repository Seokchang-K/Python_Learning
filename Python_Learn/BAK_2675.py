# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. 
# S에는 QR Code "alphanumeric" 문자만 들어있다.

test_num =  int(input())

for _ in range(test_num):
    time, word = input().split()
    for j in word:
        print(j*int(time), end='')
    print()

# 입력 예시
# 2
# 3 ABC
# 5 /HTP

# 맨처음엔 테스트 케이스의 숫자가 들어오고
# 둘째줄 부터 테스트 케이스가 들어오는데 반복횟수 문자 쌍으로 들어온다.
# for문으로 단어를 넣어주면(abc) 각 단어에 대한 처리를 진행 할 수 있다.
# a*3 b*3 c*3 이렇게
