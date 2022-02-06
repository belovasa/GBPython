"""
Задание 1
Реализовать класс Matrix (матрица).

Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков)
для формирования матрицы. В случае если список списков некорректный - возбуждать исключение ValueError с сообщением
fail initialization matrix.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

| 31 43 |
| 22 51 |
| 37 86 |

| 3 5 32 |
| 2 4 6 |
| -1 64 -8 |

| 3 5 8 3 |
| 8 3 7 1 |
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде (как показано выше).
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с
 первым элементом первой строки второй матрицы и пр.

ВНИМАНИЕ! Используйте стартовый код для своей реализации:
"""
from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        if Matrix.check_matrix_object(self, matrix):
            self.matrix = matrix
        else:
            raise ValueError('fail initialization matrix')

    def check_matrix_object(self, matrix: List[List[int]]):
        if type(matrix) is list and matrix:
            length = len(matrix[0])
            for el in matrix:
                if type(el) is list and len(el) == length:
                    continue
                else:
                    return False
        else:
            return False
        return True

    def __add__(self, other):
        matrix_sum = [[self.matrix[i][j] + other[i][j] for j in range(len(self.matrix[0]))] for i in
                      range(len(self.matrix))]
        return Matrix(matrix_sum)

    def __getitem__(self, item):
        return self.matrix[item]

    def __str__(self):
        return self.__matrix_print

    @property
    def __matrix_print(self):
        matrix_str = " "
        matrix_list = [[self.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        for el in matrix_list:
            matrix_str += f'{str(el).replace("[","|").replace("]","|")}' + '\n '
        return matrix_str


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
