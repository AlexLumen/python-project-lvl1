import random

from brain_games.games_logic import generate_number

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prepare_question_and_calculate():
    number = generate_number()
    count = 0
    question = str(number)
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count == 2:
        true_answer = 'yes'
        return true_answer, question
    else:
        true_answer = 'no'
        return true_answer, question
