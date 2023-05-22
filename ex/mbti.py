answer = input("당신은 쉬는 날에 집에 있습니까? 밖에 나갑니까? (a 또는 b로 답변하세요): ")

if answer == 'a':
    result = 'i'
elif answer == 'b':
    result = 'e'
else:
    result = 'Unknown'

print("결과:", result)