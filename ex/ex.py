questions = [
    {
        "question": "외향과 내향 중 어떤 특징이 더욱 나에게 잘 맞는 것 같나요?",
        "choices": {
            "a": "외향적인 특징",
            "b": "내향적인 특징"
        }
    },
    {
        "question": "현실적인 사고와 직관적인 사고 중 어떤 것이 더욱 편한가요?",
        "choices": {
            "a": "현실적인 사고",
            "b": "직관적인 사고"
        }
    },
    {
        "question": "사고적인 판단과 감정적인 판단 중 어떤 것을 더욱 중요하게 여기시나요?",
        "choices": {
            "a": "사고적인 판단",
            "b": "감정적인 판단"
        }
    },
    {
        "question": "계획을 세우는 것보다 즉흥적으로 일하는 것을 선호하시나요?",
        "choices": {
            "a": "즉흥적으로 일하는 것을 선호함",
            "b": "계획을 세우는 것을 선호함"
        }
    }
]

answers = []

for question in questions:
    print(question["question"])
    for choice, answer in question["choices"].items():
        print(f"{choice}. {answer}")
    user_input = input("답변을 선택하세요: ")
    answers.append(user_input)
    print()

print("선택한 답변:")
for i, answer in enumerate(answers):
    question = questions[i]["question"]
    choice = questions[i]["choices"][answer]
    print(f"{i+1}. {question} - {choice}")