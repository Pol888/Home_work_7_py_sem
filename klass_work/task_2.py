import random


def alias_generator(word_count):
    list_vowels = {ord('б'), ord('в'), ord('г'), ord('д'), ord("ж"), ord("з"), ord("к"), ord("л"), ord("м"), ord("н"),
                   ord("п"), ord("р"),
                   ord("с"), ord("т"), ord("ф"), ord("х"), ord("ц"), ord("ч"), ord("ш"), ord("щ")}
    name = ''
    name_nums = []
    for i in range(word_count):
        n = chr(random.randint(1072, 1097))
        n_2 = chr(random.randint(1100, 1103))
        v = random.randint(1, 33)
        if v == 31 or v == 32 or v == 33:
            name += n_2
            name_nums.append(ord(n_2))
        else:
            name += n
            name_nums.append(ord(n))
        for _ in range(random.randint(3, 6)):
            n_3 = chr(random.randint(1072, 1103))
            name += n_3
            name_nums.append(ord(n_3))
        name = name.capitalize()
        if len(set(name_nums).intersection(list_vowels)) > 0:
            yield name
        else:
            yield list(alias_generator(1))[0]
        name = ''




if __name__ == '__main__':
    with open('names_file.txt', 'a', encoding='utf-8') as fl:
        print(*alias_generator(22), sep='\n', file=fl)