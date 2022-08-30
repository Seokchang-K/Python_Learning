n = int(input())

a = input().split()

for i in range(n):
    a[i] = int(a[i])

number = []

# 리스트를 0으로 24개 추가한다.
for _ in range(24):
    number.append(0)

# 부른 횟수 만큼 해당 번호의 위치에 숫자를 추가해준다.
# 0 번째 부른 숫자는 예시에서 1번이고 number 리스트의 1번 인덱스에 1을 추가해준다.
for i in range(n):
    number[a[i]] += 1

# 1번 부터 23번 까지 부른 횟수를 출력해준다.
# 잊지말고 뒤에 공백을 추가해줘야 한다.
for i in range(1, 24):
    print(number[i], end=' ')