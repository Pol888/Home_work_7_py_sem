import os





def bulk_file_renaming(name_of_files, number_of_digits_in_serial_number, expansion_of_initial, expansion_of_the_final,
    index_name_start=1, index_name_end=1):

    count = 1
    serial = serial_number_generation(number_of_digits_in_serial_number, count)

    index_name_start -= 1
    index_name_end -= 1

    for i in os.listdir(os.path.join(os.getcwd())):
        name_file = i[::-1].split('.', 1)[1][::-1]
        if os.path.isfile(i) and i.split('.')[-1] == expansion_of_initial:
            new_name = ''
            if len(name_file) > index_name_end:
                new_name += name_file[index_name_start:index_name_end]
            elif len(name_file) <= index_name_end and len(name_file) > index_name_start:
                new_name += name_file[index_name_start:]
            else:
                new_name += ''

            new_name += name_of_files + serial + '.' + expansion_of_the_final
            count += 1
            serial = serial_number_generation(number_of_digits_in_serial_number, count)
            os.rename(i, new_name)



def serial_number_generation(num, count):
    return str(('0' * (num - len(str(count)))) + str(count))


