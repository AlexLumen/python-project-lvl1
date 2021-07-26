#!/usr/bin/env python
import prompt

from brain_games.hello_user import hello_user


def play(module):
    name = hello_user()
    print(module.rules)
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
