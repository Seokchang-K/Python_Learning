a, b = map(int, input().split())

a = bool(a)
b = bool(b)

print(a or b)

# 참, 거짓의 논리값 인 불(boolean) 값을 다루어주는 예약어는 not, and, or 이 있다
# or 예약어는 주어진 두 불 값 중에서 하나라도 True 이면 True 로 계산하고, 
# 나머지 경우는 False 로 계산한다.