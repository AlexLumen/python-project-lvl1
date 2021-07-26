import random

rules = "Answer 'YES' if number even otherwise answer 'NO'."


def prepare_question_and_calculate():
    number = random.randint(1, 100)
    true_answer = 'yes' if (number % 2 == 0) else 'no'
    question = str(number)
    return true_answer, question
