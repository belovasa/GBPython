"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>) . Например:

[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]
ВНИМАНИЕ! Используйте стартовый код для своей реализации:
"""
from pprint import pprint
def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    return (list_line[0], list_line[5][1:], list_line[6])
      # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    pass  # передавайте данные в функцию и наполняйте список list_out кортежами
    for line in fr:
        list_line = line.split()
        list_out.append(get_parse_attrs(list_line))
pprint(list_out)
