# 문제
# 팰린드롬은 어느 방향으로 읽어도 항상 같은 방법으로 읽을 수 있는 단어이다.
# 예를 들어, civic, radar, rotor, madam은 팰린드롬이다.
# 상근이는 단어 k개 적혀있는 공책을 발견했다. 
# 공책의 단어는 ICPC 문제가 저장되어 있는 서버에 접속할 수 있는 비밀번호에 대한 힌트이다. 
# 비밀번호는 k개의 단어 중에서 두 단어를 합쳐야 되고, 팰린드롬이어야 한다. 
# 예를 들어, 단어가 aaba, ba, ababa, bbaa, baaba일 때, ababa와 ba를 합치면 팰린드롬 abababa를 찾을 수 있다.
# 단어 k개 주어졌을 때, 팰린드롬을 찾는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
# 각 테스트 케이스의 첫째 줄에는 공책에 적혀져있는 단어의 수 k(1 ≤ k ≤ 100)가 주어진다. 
# 다음 k개 줄에는 a부터 z까지 알파벳으로 이루어진 단어가 한 줄에 하나씩 주어진다. 
# 모든 단어 길이의 합은 10,000보다 작거나 같다.

# 함수부터 작성해 보자.

def find_pel(k, words):
    for i in range(k - 1):
        # words 리스트의 첫번째 단어부터 마지막 단어 전까지만
        for j in range(i+1 , k):
            # words 리스트의 두번째 단어 부터 마지막 단어까지
            password1 = words[i] + words[j]
            # 첫단어 + 두번째 단어
            if password1 == password1[::-1]:
                # 합쳐진 두단어를 앞에서부터 읽었을 때와
                # 뒤에서 부터 읽었을 때 같다면 출력
                return password1
            
            password2 = words[j] + words[i]
            # 두번째 단어 + 첫단어
            if password2 == password2[::-1]:
                # 위와 같이 합쳤을때 앞뒤가 같다면 return
                return password2

    return 0

for i in range(int(input())):
    # 케이스의 갯수를 가져온다.
    k = int(input())
    # 단어의 수를 가져온다.
    
    # words = []
    # for _ in range(k):
    #     words.append(input())
    words = [input() for _ in range(k)]
    # 단어들을 불러와 한 리스트 안에 넣어준다.

    print(find_pel(k, words))        

        
