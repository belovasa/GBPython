"""
Задание 3
Осуществить программу работы с органическими клетками, состоящими из ячеек.

Необходимо создать класс Клетка (class Cell).
В его конструкторе инициализировать параметр cells, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:

сложение (__add__()),
вычитание (__sub__()),
умножение (__mul__()),
деление (__truediv__() и __floordiv__()).
Эти методы должны применяться только к клеткам (если это не так, необходимо возбудить исключение
TypeError с сообщением действие допустимо только для экземпляров того же класса) и выполнять увеличение,
уменьшение, умножение и оба вида деления (результаты деления должны возвращать int-значение, в случае наличия
дробной части от деления - отбрасывать её и не учитывать).

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток
 больше нуля, иначе возбуждать исключение ValueError с сообщением недопустимая операция.

Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.

Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
 ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
 Этот метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*** ...,
 где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
  ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом случае метод make_order()
 вернёт строку: *****\n*****\n**. Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда
 метод make_order() вернёт строку: *****\n*****\n*****.

Подсказка: подробный список операторов для перегрузки доступен по ссылке.

ВНИМАНИЕ! Используйте стартовый код для своей реализации:
"""

class Cell:
    def __init__(self, cells: int):
      self.cells = cells

    def erorr_decorator(method_to_decorate):
        def wrapper(self, other):
            if not isinstance(other,Cell):
                raise ValueError('Действие допустимо только для экземпляров того же класса')
            else:
                return method_to_decorate(self, other)
        return wrapper

    def make_order(self, number: int) -> str:
        result_str = ""
        i = 0
        for i in range(self.cells // number):
            result_str += f'{number * "*"} '+'\n'
            i += 1
        else: result_str +=f'{(self.cells % number) * "*"} '+'\n'
        return result_str

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if (self.cells - other.cells) <= 0:
            raise ValueError('Недопустимая операция')
        return Cell(self.cells - other.cells)

    @erorr_decorator
    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def __floordiv__(self, other):
        return self.__truediv__(other)



if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))
    """
    **********
    *****
    """

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))
    """
    ******
    ******
    *
    """

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))
    """
    ******
    ******
    """

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)  # 30

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)  # 3

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)  # 1

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)  # недопустимая операция

    try:
        cell_1 * 123
    except TypeError as err:
        print(err)  # действие допустимо только для экземпляров того же класса

