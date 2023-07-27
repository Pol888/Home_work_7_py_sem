from klass_work import task_1, task_2, task_3,  task_6, task_7
import home_work


#1
task_1.adding_a_couple_of_numbers(7, 'int_float.txt')
#2
with open('names_file.txt', 'a', encoding='utf-8') as fl:
    print(*task_2.alias_generator(3), sep='\n', file=fl)

#3
task_3.read_my_file()
#4
#task_4.file_creation('files', 'txt')
#5
#task_5.super_file_creation(4, 'txt', 'rar')
#6
task_6.super_mega_file_creation('files', 3, 'mpeg-4', 'avi', '3gp', 'jpeg', 'png', 'gif', 'txt', 'doc', 'docx', 'mp3', 'wav', 'flac', 'rar', 'xer', 'her')

#7
task_7.file_sorter(r'C:\Users\pollove\Desktop\Home_work_7_py_sem\home_work\files', 'sort_dir')
#task_home
home_work.task_home.bulk_file_renaming('new', 6, 'her', 'hhh', 1, 4)
