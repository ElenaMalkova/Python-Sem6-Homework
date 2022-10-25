# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# Новый код

res = [1.1, 1.2, 3.1, 5, 10.01]
new_res = list(map((lambda i: round(i - round(i, 0), 6)), res))
result = max(new_res) - min(new_res)
print(f'В списке {res}\nразница десятичных: {result}')


# Старый код

my_list = [1.1, 1.2, 3.1, 5, 10.01]


# Функция получения разницы долей
def get_fractions(frac_list):
    result_list = []
    for item in frac_list:  # перебираем числа в исходном списке
        int_item = round(item, 0)  # выделяем из числа целое
        # вычитаем целое, остаются доли, которые скругляем до 6 знаков
        fraction = round(item - int_item, 6)
        if fraction != 0:  # чтобы целые числа не мешались
            result_list.append(fraction)  # создаём список из долей
    # встроенными методами находим максимальное и минимальное — вычитаем
    result = max(result_list) - min(result_list)
    return result


print(f'В списке {my_list}\nразница десятичных: {get_fractions(my_list)}')
