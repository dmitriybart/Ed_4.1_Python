my_dict = {
    'key_1' : 100,
    'key_2' : 200,
    'key_3' :
    {
        'key_4': 500
    }
    }
for item in my_dict: #item - печатает ключи верхнего уровня, my_dict.values - получаем значения верхнего уровня, my_dict.items - выведет ключ и значения
    print(item) 

print(my_dict.get('key_1', '?')) # выводит значение по ключю, если нет ключа, то выведет - ?