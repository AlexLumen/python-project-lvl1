#!/usr/bin/env python
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name != '':
        print(f'Hello,{name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count != 3:
        number = random.randint(1, 1000)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if number % 2 == 0 and answer.lower() == 'no':
            print("'no' is wrong answer;(.Correct answer was 'yes'")
            print(f"Let's try again, {name}!")
            break
        elif number % 2 != 0 and answer.lower() == 'yes':
            print("'yes' is wrong answer;(.Correct answer was 'no'")
            print(f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
