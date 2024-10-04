def print_params(a = 1, b = 'строка', c = True): # задаю функцию
    print(a, b, c)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = ['Капибара', False, 3.14]
print_params(*values_list)
values_dict = {'a': True, 'c': 125, 'b': 'Кофе'}
print_params(**values_dict)
values_list_2 = [9.8, 'ответ']
print_params(*values_list_2, 42)