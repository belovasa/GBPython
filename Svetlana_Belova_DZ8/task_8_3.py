"""
Написать декоратор для логирования типов позиционных аргументов функции, например:

def type_logger...
    ...


@type_logger
def calc_cube(x):
   return x ** 3


$ a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести
тип значения функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу
декоратора? Сможете ли вывести имя функции, например, в виде:

$ a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""
from functools import wraps


def type_logger(func):
   """Я декоратор"""
   @wraps(func)
   def wrapper(*args):
      for num in args:
         print(f'{func.__name__} : ({num} : {type(num)}) ')
      result = func(*args)
      return result
   return wrapper

@type_logger
def calc_cube(x):
   """Я не декоратор"""
   return x ** 3


a = calc_cube(5.5)
print(a)

