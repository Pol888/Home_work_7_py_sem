import random


def adding_a_couple_of_numbers(count, name_file):
    with open(name_file, 'a', encoding='utf-8') as fl:
        for i in range(count):
            fl.write(f'{random.randint(-1000, 1000)}|{random.uniform(-1000.00, 1000.00)}\n')

# adding_a_couple_of_numbers(7, 'int_float.txt')
