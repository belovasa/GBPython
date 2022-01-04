"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:

$ get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.

Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)?
Сможете ли вы сделать аргументы именованными?
"""
import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []
    for i in range(count):
        list_out.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    return list_out
print(get_jokes(2))
print(get_jokes(10))

# Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы

def get_jokes_adv(count: int, fl=False) -> list:
   """
   Returns a list of jokes in count

   :param count: number of jokes
   :param fl: flag that allows or disallows repetitions
   :return: list_out
   """
   list_out = []
   unic_list = []
   if fl == True and count > min(len(nouns), len(adverbs), len(adjectives)):
      count = min(len(nouns), len(adverbs), len(adjectives))
   for i in range(count):
      random_index = random.choice(nouns)
      random_index_1 = random.choice(adverbs)
      random_index_2 = random.choice(adjectives)
      if fl == True:
         while random_index in unic_list:
            random_index = random.choice(nouns)
         while random_index_1 in unic_list:
            random_index_1 = random.choice(adverbs)
         while random_index_2 in unic_list:
            random_index_2 = random.choice(adjectives)
         unic_list.append(random_index)
         unic_list.append(random_index_1)
         unic_list.append(random_index_2)
      joke = f'{random_index} {random_index_1} {random_index_2}'
      list_out.append(joke)
   return list_out

print(get_jokes_adv(count=10, fl=True))