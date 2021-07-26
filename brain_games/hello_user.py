import prompt


def hello_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name != '':
        print(f'Hello,{name}!')
    return name
