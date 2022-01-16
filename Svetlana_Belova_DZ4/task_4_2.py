"""
В корневой директории урока создать task_4_2.py и написать в нём функцию currency_rates(),
принимающую в качестве аргумента код валюты (например, USD, EUR, SGD, ...) и
возвращающую курс этой валюты по отношению к рублю.

Использовать библиотеку requests.

В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.

Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.

Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте:
* есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
* Сильно ли усложняется код функции при этом?

Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.

Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?

В качестве примера выведите курсы доллара и евро.

"""

import requests
def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    result_value_str=''
    code = code.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if code not in response:
        return None
    result_value_str = response[response.find('<Value>', response.find(code)) + 7:response.find('</Value>', response.find(code))]
    i = result_value_str.find(',')
    result_value_str = result_value_str[:i]+'.'+result_value_str[i+1:]
    result_value = float(result_value_str)
    return result_value


print(currency_rates("USD"))
print(currency_rates("SGD"))
print(currency_rates("EUR"))
print(currency_rates("noname"))
