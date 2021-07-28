import random

from brain_games.games_logic import generate_number

RULES = "What is the result of the expression?"


def prepare_question_and_calculate():
    operations = ["+", "-", "*"]
    number_first = generate_number()
    first_number = number_first
    number_two = generate_number()
    two_number = number_two
    operation = random.choice(operations)
    operator = operation
    question = str(str(number_first) + str(operation) + str(number_two))
    true_answer = 0
    if operator == "+":
        true_answer = str(first_number + two_number)
    elif operator == "-":
        true_answer = str(first_number - two_number)
    elif operator == "*":
        true_answer = str(first_number * two_number)
    return true_answer, question
