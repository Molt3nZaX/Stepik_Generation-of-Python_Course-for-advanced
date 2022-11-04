'''Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. Напишите функцию read_csv для чтения данных
из этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую
последующую строку как значения этих ключей.

Формат выходных данных
Программа должна содержать реализованную функцию read_csv.

Примечание 1. Вызывать функцию read_csv не нужно.

Примечание 2. Функция read_csv не должна принимать аргументов.

Примечание 3. Считайте, что все ключи и значения по этим ключам в результирующем словаре имеют строковый тип (str).

Примечание 5. Если бы файл data.csv содержал информацию

name,address,age
George,4312 Abbey Road,22
John,54 Love Ave,21
то вызов функции read_csv() вернул бы список:

[{'name': 'George', 'address': '4312 Abbey Road', 'age': '22'}, {'name': 'John', 'address': '54 Love Ave', 'age': '21'}]
'''


def read_csv():
    with open('data.csv') as file:
        list_name = list(map(lambda x: x.strip(), file.readline().split(',')))

        list_all = [line.strip().split(',') for line in file.readlines()]

        total_dict = []
        for i in list_all:
            total_dict.append(dict(zip(list_name, i)))

    return total_dict

print(read_csv())
