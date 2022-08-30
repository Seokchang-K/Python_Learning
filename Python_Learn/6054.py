a, b = map(int, input().split())

a = bool(a)
b = bool(b)

print(a and b)
# and 예약어는 주어진 두 불 값이 모두 True 일 때에만 True 로 계산하고, 
# 나머지 경우는 False 로 계산한다.