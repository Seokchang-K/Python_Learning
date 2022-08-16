n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

# 먼저 위의 코드로 a라는 리스트에 문자열로 저장된 숫자들을 전부 int함수로 정수화 시킨다.

print(min(a))

# min 함수를 통해 리스트 속에서 가장 작은값을 출력한다.