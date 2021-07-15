#!/usr/bin/env python
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name != '':
        print(f'Hello,{name}!')
    print('What is the result of the expression?')
    count = 0
    operations = ["+", "-", "*"]
    while count != 3:
        number_first = random.randint(1, 10)
        first_number = number_first
        number_two = random.randint(1, 10)
        two_number = number_two
        operation = random.choice(operations)
        operator = operation
        true_result = 0
        print(f'Question: {number_first} {operation} {number_two}')
        if operator == "+":
            true_result = str(first_number + two_number)
        elif operator == "-":
            true_result = str(first_number - two_number)
        elif operator == "*":
            true_result = str(first_number * two_number)
        answer = prompt.string('Your answer: ')
        if true_result != answer:
            print(f"'{answer}' is wrong answer;(.Correct answer was '{true_result}'")
            print(f"Let's try again, {name}!")
            break
        else:
            print("Correct!")
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
