#!/usr/bin/env python
import prompt


def hello_user(module):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    if user_name != '':
        print(f'Hello,{user_name}!')
    return user_name


def logic_games(module):
    name = hello_user(module)

