print('"Функция с параметрами по умолчанию:"')
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(3, 'string', False)
print_params(52, 'Uran')
print_params(12)
print_params(b=25)
print_params(c=[1, 2, 3])
print('"Распаковка параметров:"')
values_list = [67, 'string', True]
values_dict = {'a': 37, 'b': 'my', 'c': False}
print_params(*values_list)
print_params(**values_dict)
print('"Распаковка + отдельные параметры:"')
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)