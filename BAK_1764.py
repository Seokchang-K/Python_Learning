# 문제
# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 
# 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 
# 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.
# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

n, m = map(int, input().split())

# 듣도 못한 사람
# n_hear = []
# for _ in range(n):
#     n_hear.append(input())
# -> 시간초과

# n_hear = [input() for _ in range(n)] -> 시간초과

n_hear = {input(): 1 for _ in range(n)}
# -> 시간초가 발생하지 않음.

# 보도 못한 사람
n_see_hear = []

for _ in range(m):
    n_see = input()
    if n_see in n_hear:
        n_see_hear.append(n_see)

# print(len(n_see_hear), *n_see_hear, sep='\n') 
# -> 자꾸 오답이 발생 why? 사전 순으로 출력해야됨.
print(len(n_see_hear), *sorted(n_see_hear), sep='\n')
