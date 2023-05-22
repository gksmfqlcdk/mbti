answer = input("당신의 좋아하는 계절은 무엇인가요?: ")

if answer == "봄":
    result = "봄은 꽃이 피는 아름다운 계절입니다."
elif answer == "여름":
    result = "여름은 해변에서 즐거운 시간을 보낼 수 있는 계절입니다."
elif answer == "가을":
    result = "가을은 단풍이 아름답고 시원한 바람이 불어오는 계절입니다."
elif answer == "겨울":
    result = "겨울은 눈이 내려 따뜻한 차를 마시며 즐길 수 있는 계절입니다."
else:
    result = "좋아하는 계절을 선택해주세요."

print("결과:", result)