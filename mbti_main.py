MBTI = [None] * 4
pntmbti = [None] * 4

while MBTI[0] not in ['A', 'a', 'B', 'b']:
    MBTI[0] = input("당신은 쉬는 날에\nA: 밖에서 논다 / B: 집에 있는다\n")
    if MBTI[0] in ['a', 'A']:
        pntmbti[0] = 'E'
    elif MBTI[0] in ['b', 'B']:
        pntmbti[0] = 'I'

while MBTI[1] not in ['C', 'c', 'D', 'd']:
    MBTI[1] = input("사과를 보면?\nC: 빨갛다 / D: 사과는 왜 나무에서 자랄까?\n")
    if MBTI[1] in ['c', 'C']:
        pntmbti[1] = 'S'
    elif MBTI[1] in ['d', 'D']:
        pntmbti[1] = 'N'

while MBTI[2] not in ['E', 'e', 'F', 'f']:
    MBTI[2] = input("나 우울해서 화분을 샀어의 대답은?\nE: 왜 우울해? / F: 무슨 화분 샀는데?\n")
    if MBTI[2] in ['E', 'e']:
        pntmbti[2] = 'F'
    elif MBTI[2] in ['F', 'f']:
        pntmbti[2] = 'T'

while MBTI[3] not in ['G', 'g', 'H', 'h']:
    MBTI[3] = input("방학 계획을 세울 때 나는?\nG: 어떤 일이 벌어질지 모른다 / H: 시간별로 계획을 나눈다\n")
    if MBTI[3] in ['G', 'g']:
        pntmbti[3] = 'P'
    elif MBTI[3] in ['H', 'h']:
        pntmbti[3] = 'J'

for i in range(4):
    print(pntmbti[i],end="")