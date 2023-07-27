import random
import os



def file_creation(name_dir, file_extension, min_len_name=4, max_len_name=30, min_write_byt=256, max_write_byt=4096,
                  number_of_files=42):
    for _ in range(number_of_files):
        name = ''
        for i in range(random.randint(min_len_name, max_len_name)):
            name += chr(random.randint(97, 122))
        name += '.' + file_extension
        flag = True
        while flag:
            if name in os.listdir(os.path.join(os.getcwd(), name_dir)):
                name = chr(random.randint(97, 122)) + name[1:]
            else:
                flag = False
        with open(os.path.join(os.getcwd(), name_dir, name), 'w', encoding='utf=8') as fl:
            fl.write('1' * random.randint(min_write_byt, max_write_byt))



