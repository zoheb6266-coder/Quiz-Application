import random

# Question Bank
questions = [
    {
        "question": "Which keyword is used to define a function?",
        "options": {
            "A": "func",
            "B": "def",
            "C": "function",
            "D": "lambda"
        },
        "answer": "B"
    },
    {
        "question": "What is the value of len('Hi')?",
        "options": {
            "A": "1",
            "B": "2",
            "C": "3",
            "D": "4"
        },
        "answer": "B"
    },
    {
        "question": "Which is a mutable data type?",
        "options": {
            "A": "tuple",
            "B": "str",
            "C": "list",
            "D": "int"
        },
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": {
            "A": "//",
            "B": "#",
            "C": "/*",
            "D": "&"
        },
        "answer": "B"
    },
    {
        "question": "Which function displays output?",
        "options": {
            "A": "input()",
            "B": "print()",
            "C": "show()",
            "D": "display()"
        },
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": {
            "A": "int",
            "B": "str",
            "C": "bool",
            "D": "list"
        },
        "answer": "C"
    },
    {
        "question": "Which loop is used to iterate over a list?",
        "options": {
            "A": "for",
            "B": "switch",
            "C": "define",
            "D": "case"
        },
        "answer": "A"
    },
    {
        "question": "Which brackets are used to create a list?",
        "options": {
            "A": "()",
            "B": "{}",
            "C": "[]",
            "D": "<>"
        },
        "answer": "C"
    },
    {
        "question": "Which operator is used for equality comparison?",
        "options": {
            "A": "=",
            "B": "==",
            "C": "!=",
            "D": "+"
        },
        "answer": "B"
    },
    {
        "question": "Which module helps select random items?",
        "options": {
            "A": "math",
            "B": "os",
            "C": "random",
            "D": "time"
        },
        "answer": "C"
    }
]


def run_quiz():
    score = 0
    total = len(questions)

    # Randomly select 3 questions
    selected_questions = random.sample(
        questions, min(3, total)
    )

    print("\n================================")
    print("       QUIZ APPLICATION")
    print("================================")
    print("Answer the following questions.")
    print("Enter A, B, C or D.")
    print("Passing Marks: 50%")
    print("================================")

    for number, item in enumerate(selected_questions, start=1):
        print(f"\nQ{number}. {item['question']}")

        for key, value in item["options"].items():
            print(f"  {key}. {value}")

        while True:
            answer = input("Your answer: ").strip().upper()

            if answer not in ["A", "B", "C", "D"]:
                print("Invalid option. Enter A, B, C or D.")
                continue

            break

        if answer == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print(
                f"Wrong. Correct answer: {item['answer']}"
            )

    percentage = (score / len(selected_questions)) * 100

    print("\n================================")
    print("          QUIZ RESULT")
    print("================================")
    print(f"Score: {score}/{len(selected_questions)}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 50:
        print("Result: Pass")
    else:
        print("Result: Fail")

    print("================================")


if __name__ == "__main__":
    run_quiz()