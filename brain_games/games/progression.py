import random

RULES = "What number is missing in the progression?"


def prepare_question_and_calculate():
    progression_list = []
    number = random.randint(1, 20)
    iterator = random.randint(1, 10)
    for _ in range(10):
        progression_list.append(str(number))
        number += iterator
    elem_for_replace = \
        progression_list[random.randint(1, len(progression_list))]
    for (index, elem) in enumerate(progression_list):
        if progression_list[index] == elem_for_replace:
            progression_list[index] = '..'
            break
    progression = ''
    for (index, elem) in enumerate(progression_list):
        progression += progression_list[index]
        progression += ' '
    progression = progression.rstrip(' ')
    question = progression
    true_answer = elem_for_replace
    return true_answer, question
