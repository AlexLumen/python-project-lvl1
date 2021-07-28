import random

from brain_games.games_logic import generate_number

RULES = "Answer 'YES' if number even otherwise answer 'NO'."


def prepare_question_and_calculate():
    number = generate_number()
    true_answer = 'yes' if (number % 2 == 0) else 'no'
    question = str(number)
    return true_answer, question
