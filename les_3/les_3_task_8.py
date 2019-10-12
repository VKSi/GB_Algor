# Vasilii Sitdikov
# GeekBrains Courses. Algorithms
# Lesson 3 task 8
# October 2019

# task: 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
#       Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
#       В конце следует вывести полученную матрицу.

# Solution:
# Заполнение матрицы
matrix = [['' for _ in range(4)] for _ in range(5)]

for i in range(5):
    res = 0  # Переменная для хранения временной суммы
    for j in range(3):  # Последний элемент строки не заполняем
        matrix[i][j] = float(input(f'Введите значение элемента для {j}-го элемента {i}-ой строки матрицы: '))
        res += matrix[i][j]  # Добавляем новый элемент в сумму
    matrix[i][3] = res  # После ввода всех элементов строки записываем результат в последнюю ячейку
    print()

# Вывод матрицы на экран
print("Сформирована матрица:")
print('*' * len(matrix[0]) * 5)
for row in matrix:
    for item in row:
        print(f'{item:>5}', end='')
    print()
print('*' * len(matrix[0]) * 5)
