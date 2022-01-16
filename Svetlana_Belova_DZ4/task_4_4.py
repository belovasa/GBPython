"""
Написать свой модуль utils и копировать в него функцию currency_rates() из предыдущего задания.

Создать в корневой директории урока, рядом с модулем utils скрипт task_4_4.py, в котором импортировать модуль
utils и выполнить несколько вызовов функции utils.currency_rates().

Убедиться, что ничего лишнего не происходит.

Приложите в конце скрипта task_4_4.py многострочным комментарием результат его запуска с консоли/терминала.
"""
import utils

print(utils.currency_rates('USD'))
print(utils.currency_rates('EUR'))
print(utils.currency_rates("noname"))
"""
75.7668
86.8894
None

Process finished with exit code 0

"""