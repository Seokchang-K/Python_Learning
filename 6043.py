a, b = map(float, input().split())

out = a/b

out = round(out, 3)

print('%0.3f' % out)

# 무조건 소수점 3째 자리까지 나와야 하기에 
# '%0.3f' 을 넣어 포멧을 만들어준다.