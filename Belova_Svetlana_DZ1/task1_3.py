"""
Реализовать склонение слова процент во фразе N процентов.
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов

"""
def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    if (number >= 5 and number <= 19) or (number % 10 >= 5 and number % 10 <= 9) or (number % 10 == 0):
        return(f'{number} процентов')
    elif (number >= 2 and number <= 4) or (number % 10 >= 2 and number % 10 <= 4):
        return(f'{number} процента')
    elif number == 1 or number % 10 == 1:
        return(f'{number} процент')

for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
