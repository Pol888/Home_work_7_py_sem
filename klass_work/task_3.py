def read_my_file():
    with (open('int_float.txt', 'r', encoding='utf-8') as num_fl,
          open('names_file.txt', 'r', encoding='utf-8') as names_fl,
          open('names_and_num.txt', 'a', encoding='utf-8') as n_a_n):
        nums = [int(i[:-1].split('|')[0]) * float(i[:-1].split('|')[1]) for i in num_fl.readlines()]
        names = [i[:-1] for i in names_fl.readlines()]

        index_nums = 0
        index_names = 0
        result = []
        flag = ''
        while flag != 'end':
            if nums[index_nums] < 0:
                result.append(f'{names[index_names].lower()}:{abs(nums[index_nums])}\n')

            else:
                result.append(f'{names[index_names].lower()}:{int(nums[index_nums])}\n')

            index_nums += 1
            index_names += 1

            if index_nums == len(nums) and flag == '':
                index_nums = 0
                flag = 'names'
            elif index_names == len(names) and flag == '':
                index_names = 0
                flag = 'nums'

            elif flag == 'names' and index_nums == len(nums) - 1:
                index_nums = -1
            elif flag == 'nums' and index_names == len(names) - 1:
                index_names = -1

            elif flag == 'names' and index_names == len(names):
                flag = 'end'
            elif flag == 'nums' and index_nums == len(nums):
                flag = 'end'

        n_a_n.writelines(result)

#read_my_file()