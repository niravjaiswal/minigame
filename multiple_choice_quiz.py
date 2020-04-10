from multiple_choice_quiz2 import Question

question_promts = [
    "What color are strawberries?\n(a) Red\n (b) Orange\n (c) Aquamarine\n\n"
    "What color are lemons?\n(a) Pink\n (b) Cyan\n (c) Yellow\n\n"
    "What color are oranges?\n(a) Yellow\n (b) Orange\n (c) Magenta\n\n"
]

questions = [
    Question(question_promts[0], "a"),
    Question(question_promts[1], "c"),
    Question(question_promts[2], "b")
]

def run_test(questions):
    score = 0
    for _ in questions:
        answer = input(Question.prompt)
        if answer == Question.answer:
            score += 1

    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

run_test(questions)