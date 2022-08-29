# 문제
# 네오와 프로도가 숫자놀이를 하고 있습니다. 
# 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.
# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"

# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. 
# s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.
# 참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.


# 입출력 예
# "one4seveneight"	-> 1478
# "23four5six7"	-> 234567
# "2three45sixseven"	-> 234567
# "123"	123

def solution(s):
    plate = {
    '0':'zero',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine'
}
    # 먼저 서로 대응되는 딕셔너리를 지정해 준다.

    for n, e in plate.items():
        # n = 숫자
        # e = 영어
        # 딕셔너리의 Key 와 Velue를 items 를 이용해 불러온다.
        s = s.replace(e,n)
        # replace 함수를 이용해 문장에서의 영단어 e 을 숫자 n 으로 바꿔준다.
    
    return int(s)
    # 변환된 s를 return 해주며 숫자로만 이루어진 문자열 s를 int()함수로 정수화시켜 준다.
