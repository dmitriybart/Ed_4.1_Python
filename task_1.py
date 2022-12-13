# Работа с файлами tuple(кортежи), set(списки), dict(словари/множества)
# 'w' - персоздает/создает запись
# 'r' - чтение
# 'a' - дозапись в конец файла
# 'r+' - чтение+дозапись


# f = open('test.txt', 'w')
# f.write('Hello world!')
# f.close


# file_path = r'test.txt' #сырая строка, преобразует путь к файлу в норм вид
# with open(file_path, 'r') as f_data:
#     print(f_data.read())

# Считать строку из набора чисел из файла. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел. Результат заисать в конец исходного файла (х1 х2

##ДЛИННЫЙ ВАРИАНТ

# with open ('file.txt', 'w') as data:
#     data.write('2 5 7 10 3\n')
# with open ('file.txt', 'r') as data:
#     lst = data.read()
# new_lst = lst.split()
# lst_int = [int(i) for i in new_lst]
# max_num = max(lst_int)
# min_num = min(lst_int)
# with open ('file.txt', 'a') as data:
#     data.write(f'max = {max_num}, min = {min_num}')

##КОРОТКИЙ ВАРИАНТ

with open('file.txt', 'r') as text_file:
    data_list = list(map(int, text_file.readline().split()))
with open('file.txt', 'a') as text_file:
    text_file.write(f'max = {max(data_list)}, min = {min(data_list)}\n') # ПЕЧАТАЕТ В ФАЙЛЕ
    #print(f'max = {max(data_list)}, min = {min(data_list)}') ВЫВОД В КОНСОЛЬ