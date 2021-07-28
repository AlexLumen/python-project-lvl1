import random

RULES = "Find the greatest common divisor of given numbers."


def prepare_question_and_calculate():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    numerator = max(first_number, second_number)
    denominator = min(first_number, second_number)
    quotient = numerator % denominator
    while quotient != 0:
        numerator = denominator
        denominator = quotient
        quotient = numerator % denominator
    nod = denominator
    true_answer = str(nod)
    question = (str(first_number), str(second_number))
    return true_answer, question
