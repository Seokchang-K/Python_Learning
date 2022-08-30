n = int(input())
a = input().split()

for i in range(n):
  a[i] = int(a[i])

# 위의 코드를 통해 문자열로 리스트 a에 저장된 숫자들을 정수형으로 바꿔준다.

for i in range(n-1, -1, -1):
  print(a[i], end=' ')

# range(n-1, -1, -1):
# 위 코드의 의미는 
# start n-1 번 즉 9번 부터 
# end -1 까지 즉 0번까지
# -1 즉 역순으로 진행하라는 뜻이다. 