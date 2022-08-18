# 첫째 줄에는 스위치 개수가 주어진다. 스위치 개수는 100 이하인 양의 정수이다. 
# 둘째 줄에는 각 스위치의 상태가 주어진다. 켜져 있으면 1, 꺼져있으면 0이라고 표시하고 사이에 빈칸이 하나씩 있다. 
# 셋째 줄에는 학생수가 주어진다. 학생수는 100 이하인 양의 정수이다. 
# 넷째 줄부터 마지막 줄까지 한 줄에 한 학생의 성별, 학생이 받은 수가 주어진다. 
# 남학생은 1로, 여학생은 2로 표시하고, 학생이 받은 수는 스위치 개수 이하인 양의 정수이다. 
# 학생의 성별과 받은 수 사이에 빈칸이 하나씩 있다.

def trun(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

switch_n = int(input())

switch = [9] + list(map(int, input().split()))

student_n = int(input())

for _ in range(student_n):
    sex, num = map(int,input().split())

    if sex == 1:
        for i in range(num, switch_n+1, num):
            trun(i)
    
    else:
        trun(num)
        for j in range(switch_n//2):
            if num + j > switch_n or num + j < 1 : break
            
            if switch[num + j] == switch[num - j]:
                trun(num + j)
                trun(num - j)
           
            else:
                break

for i in range(1, switch_n+1):
    print(switch[i], end=' ')
    if i%20 == 0 :
        print()
