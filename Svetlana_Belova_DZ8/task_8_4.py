"""
Задание 4
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения
функции и выбрасывать исключение ValueError, если что-то не так, например:

$ calc_cube(5)
125
$ calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
Примечание: сможете ли вы замаскировать работу декоратора?

ВНИМАНИЕ! Используйте стартовый код для своей реализации:
"""
from functools import wraps


def val_checker(qwe = lambda x:x):
   def _logger(func):
        @wraps(func)
        def wrapper(args):
            msg =''
            if qwe(args):
               result = func(args)
               msg = f'{func.__name__} -> {result}'
            else:
                msg = f'wrong val {args}'
                raise ValueError(msg)
            return msg
        return wrapper
   return _logger


@val_checker(lambda x: x > 0)  # не забудьте про аргумент-функцию
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
#    print(calc_cube('ss'))
