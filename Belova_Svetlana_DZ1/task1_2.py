"""
a) Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):

Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

Например, число `19 ^ 3 = 6859` будем включать в сумму, так как `6 + 8 + 5 + 9 = 28` – делится нацело на `7`. 
Внимание: использовать только арифметические операции!

b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых
делится нацело на 7.

*c) Решить задачу под пунктом b, не создавая новый список. (если будете решать - либо создайте доп. функцию, либо
перепишите существующую sum_list_2)

ВНИМАНИЕ! Используйте стартовый код для своей реализации:

def sum_list_1(dataset: list) -> int:
    Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"
    # место для написания кода
    return 1  # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
   '""К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7""
    # место для написания кода
    return 1  # Верните значение полученной суммы

"""
def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    indx = 0
    tran_str = ''
    result = 0
    while indx < len(dataset):
        tran_str = str(dataset[indx])
        sum_cub = 0
        j = 0
        for j in range(len(tran_str)):
            sum_cub = sum_cub + int(tran_str[j])
            j += 1
        if sum_cub % 7 == 0:
           result += dataset[indx]
        indx += 1
    return result

def sum_list_2(dataset: list) -> int:
   """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
   for i, num_cub in enumerate(dataset):
      dataset[i] = num_cub + 17
   indx = 0
   tran_str = ''
   result = 0
   while indx < len(dataset):
      tran_str = str(dataset[indx])
      sum_cub = 0
      j = 0
      for j in range(len(tran_str)):
         sum_cub = sum_cub + int(tran_str[j])
         j += 1
      if sum_cub % 7 == 0:
         result += dataset[indx]
      indx += 1
   return result



my_list = []
i = 0
for i in range(1, 1000, 2):
    my_list.append(i**3)
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)









