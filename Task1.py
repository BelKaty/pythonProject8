"""Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18"""

class Matrix:
    def __init__(self, list_of_lists):
        self.matr = list_of_lists

    def __str__(self):
        string = ''
        for i in self.matr:
            for j in i:
                string = string + '%s\t' % (j)
            string = string[:-1]
            string = string + '\n'
        string = string[:-1]
        return string

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.matr)):
            for j in range(len(self.matr[0])):
                sum = other.matr[i][j] + self.matr[i][j]
                numbers.append(sum)
                if len(numbers) == len(self.matr[0]):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matr1 = Matrix(x)
matr2 = Matrix(y)

print(matr1.__str__())
print("+")
print(matr2.__str__())
print("__________")
print(matr1 + matr2)