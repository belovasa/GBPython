"""
Задание 1
Написать тело функцию email_parse(email: str), которая при помощи регулярного выражения извлекает имя пользователя и
почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение ValueError.
Пример:

$ email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
$ email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
ВНИМАНИЕ! Используйте стартовый код для своей реализации:
"""
import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    out_dict = {}
    RE_MAIL = re.compile(r'(\w+)+@(\w+\.+\w+)')
    match = RE_MAIL.search(email)
    if match:
        out_dict = re.match(r'(?P<username>(\w+))+@+(?P<domain>(\w+\.+\w+))', email).groupdict()
    else:
        raise ValueError('Адрес введен неверно')
    return out_dict


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    email_parse('someone@geekbrainsru')


