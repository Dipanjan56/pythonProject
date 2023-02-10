from random import choice


def baby_conversion():
    list_questions = ["why a?: ", "why b?: ", "why c?: "]
    question = choice(list_questions)
    answer = input(question).strip().lower()
    print(answer)

    while answer != "just because":
        answer = input("why?: ").strip().lower()


if __name__ == '__main__':
    baby_conversion()
