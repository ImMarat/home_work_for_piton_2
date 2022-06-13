"""1. Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2"""

print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))

"""2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число
(вещественные не трогаем) кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом)
и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел со знаком?
Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже. 
Главное: дополнить числа до двух разрядов нулём!
"""

init_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
transformed_list = []

for element in init_list:
    if element[0] in ['-', '+']:
        element = ['"', f"{element[0]}{int(element[1:]):02d}", '"']
    else:
        if element.isnumeric():
            element = ['"', f"{int(element):02d}", '"']
        else:
            element = [element]
    transformed_list.extend(element)

# *3 задание

i = 0

while i < len(init_list):
    element = init_list[i]
    if element[0] in ['-', '+']:
        init_list[i] = f"{element[0]}{int(element[1:]):02d}"
        init_list.insert(i+1, '"')
        init_list.insert(i, '"')
        i += 1

    else:
        if element.isnumeric():
            init_list[i] = f"{int(element):02d}"
            init_list.insert(i+1, '"')
            init_list.insert(i, '"')
            i += 1
    i += 1

res_str = ''
for element in init_list:
    if element[0] in ['-', '+']:
        res_str += f'"{element[0]}{int(element[1:]):02d}" '
    else:
        if element.isnumeric():
            res_str += f'"{int(element):02d}" '
        elif element != '"':
            res_str += f'{element} '

print(res_str)

