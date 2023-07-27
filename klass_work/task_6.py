import klass_work.task_4
import os



def super_mega_file_creation(name_dir, count_files, *args):
    if name_dir in os.listdir():
        for i in args:
            klass_work.task_4.file_creation(name_dir, i, number_of_files=count_files)
    else:
        os.mkdir(name_dir)
        for i in args:
            klass_work.task_4.file_creation(name_dir, i, number_of_files=count_files)

#super_mega_file_creation('files', 3, 'mpeg-4', 'avi', '3gp', 'jpeg', 'png', 'gif', 'txt', 'doc', 'docx', 'mp3', 'wav', 'flac', 'rar', 'xer', 'her')