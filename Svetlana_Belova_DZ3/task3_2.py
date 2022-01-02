"""
*(вместо задачи 1) Перепишите функцию из задания 1 изменив название на num_translate_adv():
реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
должен быть с заглавной.

"""
def num_translate_adv(value: str) -> str:
    """переводит числительное с английского на русский """
    dic_number = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
                  'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                  'seven': 'семь', 'eight': 'восемь', 'nine': 'девять',
                  'ten': 'десять'}
    if value.istitle():
       str_out = '"'+dic_number.get(value.lower()).capitalize()+'"'
    else:
       str_out = '"'+dic_number.get(value)+'"'
    return str_out


print(num_translate_adv("One"))

print(num_translate_adv("two"))
