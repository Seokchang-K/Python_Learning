a = input()

a = ord(a)
b = ord('a')

while b<=a:
    print(chr(b), end=' ')
    b = b + 1

# 알파벳 문자 a의 정수값은 ord('a')로 알아낼 수 있다.
# chr(정수값)을 이용하면 유니코드 문자로 출력할 수 있다.