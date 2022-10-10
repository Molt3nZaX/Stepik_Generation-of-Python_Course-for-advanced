'''
Магический квадрат 🌶️

Магическим квадратом порядка nn называется квадратная таблица размера n×n, составленная из всех чисел 1, 2, 3, ... n^2
так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу,
которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных:
На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы: n строк,
по n чисел в каждой, разделённые пробелами.

Формат выходных данных:
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.


Sample Input 1:
3
8 1 6
3 5 7
4 9 2

Sample Output 1:
YES

Sample Input 2:
3
8 2 6
3 5 7
4 9 1

Sample Output 1:
NO
'''

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
main_diag = 0
secondary_diag = 0
total_string = 0
total_post = 0
total_matrix = 0
l, m = 0, 0
for k in range(n):  # подсчет суммы всех элементов
    for j in range(n):
        total_matrix += matrix[k][j]

if total_matrix != (n ** 2 * (n ** 2 + 1)) / 2:  # проверка матрицы на сумму квадратов всех элементов
    flag = False
elif matrix[0][1] == matrix[l][m]:
    flag = False
else:
    for i in range(n):
        main_diag += matrix[i][i]  # сумма элементов основной диагонали
        secondary_diag += matrix[n - i - 1][i] # сумма элементов второстепенной диагонали

    for string in matrix:  # подсчет суммы элементов каждой из строк и сравление с основной диагональю
        total_string = sum(string)
        if total_string == main_diag and total_string == secondary_diag:
            flag = True
        else:
            flag = False
            break

    for k in range(n):  # подсчет суммы элементов столбцов
        for j in range(n):
            total_post += matrix[j][k]
        if total_post == total_string:
            flag = True
            total_post = 0
        else:
            flag = False
            break

if flag:
    print('YES')
else:
    print('NO')
