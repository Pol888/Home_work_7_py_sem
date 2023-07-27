from task_4 import file_creation


def super_file_creation(count_files, *args):
    for i in args:
        file_creation(i, number_of_files=count_files)

