#!/usr/bin/env python
import prompt
from random import randint


def hello_user():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name?')
    print(f'Hello, {user_name}!')
    return user_name


def generate_number():
    """Return random number from range."""
    return randint(1, 100)


def play(module):
    name = hello_user()
    print(module.RULES)
    count = 0
    while count != 3:
        answer_true, question = module.prepare_question_and_calculate()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if answer_true != user_answer.lower():
            print(f'{user_answer} is wrong'
                  f' answer;(.Correct answer was {answer_true}')
            print(f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
            count += 1
        if count == 3:
            print(f'Congratulations, {name}!')
