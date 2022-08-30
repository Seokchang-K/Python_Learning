# 두 단어 A와 B가 주어진다. A는 가로로 놓여야 하고, B는 세로로 놓여야 한다. 
# 또, 두 단어는 서로 교차해야 한다. (정확히 한 글자를 공유해야 한다) 
# 공유하는 글자는 A와 B에 동시에 포함되어 있는 글자여야 하고, 그런 글자가 여럿인 경우 A에서 제일 먼저 등장하는 글자를 선택한다. 
# 마찬가지로 이 글자가 B에서도 여러 번 등장하면 B에서 제일 처음 나오는 것을 선택한다.

# 입력
# 첫째 줄에 두 단어 A와 B가 주어진다. 두 단어는 30글자 이내이고, 공백으로 구분되어져 있다. 
# 또, 대문자로만 이루어져 있고, 적어도 한 글자는 두 단어에 포함되어 있다.

# 입력 예시
# BANANA PIDZAMA

word1, word2 = input().split()

# enumerate!
# 만약 단어를 넣고 i 와 char를 변수로 주고 enumerate를 사용한다면!
# word 라는 단어를 넣었을 경우
# 0 w, 1 o, 2 r, 3 d
# 이런식으로 글자의 인덱스 넘버를 변수에 지정해 준다.
# 만약에 i 와 char를 넣지 않고, i 만 넣는 다면!
# (0, w), (1, o), (2, r), (3, d) 이런식의 튜플 형태로 할당된다.

# 겹치는 부분 찾기
for i, char in enumerate(word1):
    # 이렇게 인덱스 넘버와 각 단어를 짝지어 줬다.
    position_b = word2.find(char)
    # word2 에서 find(char)를 통해 일치하는 단어가 있으면 그 인덱스 넘버를 받아와 준다.
    # 즉 word1 과 word2 의 단어중 일치하는 가장 앞글자의 위치를 찾아준다.(word2의 단어 중)
    if position_b != -1:
        # 만약에 b의 단어 위치가 맨 마지막이 아니라면 
        # word1 의 단어중 일치하는 단어의 인덱스 넘버를 position_a 에 할당해주고, break해준다.
        position_a  = i
        break

# 출력 부분
for i, char in enumerate(word2):
    if i == position_b:
        # word2 에대해서 만약 position_b 의 인덱스 값과 일치하는 인덱스 값을 지닌 i 가 오게되면
        # word1 을 출력한다.
        print(word1)
    else:
        # 만약 i 와 position_b의 인덱스 값이 같지 않다면
        # word1에서의 인덱스 값까지 . 을 찍고 word2의 char 를 쓴다음 word1의 단어 마지막까지 . 을찍어준다.
        print("." * position_a + char + "." * (len(word1) - position_a - 1))