'''Random name and surname

Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.

Напишите программу, которая c помощью модуля random создает 33 случайные пары имя + фамилия, а затем выводит их,
каждую на отдельной строке.

Формат входных данных:
На вход программе ничего не подается.

Формат выходных данных:
Программа должна вывести текст в формате, приведенном в примере.

Пример:
Abdul Albertson
Abel Adamson
Albert Einstein'''


from random import choices


with open('first_names.txt') as first_names, open('last_names.txt') as last_names:
    choi_last, choi_first = map(lambda x: x.rstrip(), choices(first_names.readlines(), k=3)), \
                            map(lambda x: x.rstrip(), choices(last_names.readlines(), k=3))
    zip_list = zip(choi_first, choi_last)
    print(*map(lambda x: f'{x[1]} {x[0]}', zip_list), sep='\n')