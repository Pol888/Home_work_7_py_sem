import os
import shutil


def file_sorter(sort_path, name_to_create_directory):
        new_cat = os.getcwd()
        os.makedirs(f'{name_to_create_directory}/video')
        os.makedirs(f'{name_to_create_directory}/foto')
        os.makedirs(f'{name_to_create_directory}/text')
        os.makedirs(f'{name_to_create_directory}/music')
        os.chdir(sort_path)
        for i in os.listdir():
            if os.path.isfile(i):
                extension = i.split('.')[-1]
                #os.chmod(i, mode=stat.S_IROTH)
                if extension in ['mpeg-4', 'avi', '3gp']:
                    shutil.copy2(i, os.path.join(new_cat, name_to_create_directory, 'video'))
                    os.remove(i)
                        #os.replace(i, os.path.join(new_cat, name_to_create_directory, 'video'))
                elif extension in ['jpeg', 'png', 'gif']:
                    shutil.copy2(i, os.path.join(new_cat, name_to_create_directory, 'foto'))
                    os.remove(i)
                        #os.replace(i, os.path.join(new_cat, name_to_create_directory, 'foto'))
                elif extension in ['txt', 'doc', 'docx']:
                    shutil.copy2(i, os.path.join(new_cat, name_to_create_directory, 'text'))
                    os.remove(i)
                        #os.replace(i, os.path.join(new_cat, name_to_create_directory, 'text'))
                elif extension in ['mp3', 'wav', 'flac']:
                    shutil.copy2(i, os.path.join(new_cat, name_to_create_directory, 'music'))
                    os.remove(i)
                        #os.replace(i, os.path.join(new_cat, name_to_create_directory, 'music'))


#file_sorter(r'C:\Users\pollove\Desktop\Home_work_7_py_sem\klass_work\files', 'new_cat')