total_list = {}

while True: #break를 만나기 전까지 코드를 무한히 반복한다
    question = input("질문을 입력해주세요: ")
    if question == "q":
        break
    else:
        total_list.append({"질문" : question, "답변" : ""})

for i in total_list:
    print(i["질문"])
    answer = input("답변을 입력해주세요")
    i["답변"] = answer

print(total_dictionary)