a = 42
b = 'Hello world!'
c = [1, 3, 5, 7]
my_list = [None]
my_list.append(a)
print(my_list)
my_list.append(b)
print(my_list)
my_list.append(c)
print(my_list)

print("------------------")

a = 42
b = 'Hello world!'
c = [1, 3, 5, 7]
my_list = [None]
#my_list.extend(a) # TypeError: 'int' object is not iterable
print(my_list)
my_list.extend(b)
print(my_list)
my_list.extend(c)
print(my_list)
my_list.extend(my_list)
print(my_list)

print("------------------")

my_list = [2, 4, 6, 8, 10, 12]
spam = my_list.pop()
print(spam, my_list)
eggs = my_list.pop(1)
print(eggs, my_list)
#err = my_list.pop(10) # IndexError: pop index out of range

print("------------------")

my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
spam = my_list.count(2)
print(spam)
eggs = my_list.count(3)
print(eggs)

print("------------------")

my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
spam = my_list.index(4)
print(spam)
eggs = my_list.index(4, spam + 1, 90)
print(eggs)
#err = my_list.index(3) # ValueError: 3 is not in list

print("------------------")

my_list = [2, 4, 6, 8, 10, 12]
my_list.insert(2, 555)
print(my_list)
my_list.insert(-2, 13)
print(my_list)
my_list.insert(55, 73) # my_list.append(73)
print(my_list)

print("------------------")

my_list = [2, 4, 6, 8, 10, 12, 6]
my_list.remove(6)
print(my_list)
my_list.remove(6) # ValueError: list.remove(x): x not in list
print(my_list)

print("------------------")

my_list = [4, 8, 2, 9, 1, 7, 2]
sort_list = sorted(my_list)
print(my_list, sort_list, sep='\n')
rev_list = sorted(my_list, reverse=True)
print(my_list, rev_list, sep='\n')

print("------------------")

my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

print("------------------")

my_list = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list)
print(type(res), res)
rev_list = list(reversed(my_list))
print(rev_list)

print("------------------")

for item in reversed(my_list):
    print(item)

print("------------------")

my_list = [4, 8, 2, 9, 1, 7, 2]
my_list.reverse()
print(my_list)

print("------------------")

my_list = [4, 8, 2, 9, 1, 7, 2]
new_list = my_list[::-1]
print(my_list, new_list, sep='\n')

print("------------------")

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
print(my_list[2:7:2])
print(my_list[:7:2])
print(my_list[2::2])
print(my_list[2:7:])
print(my_list[8:3:-1])
print(my_list[3::])
print(my_list[:7:])

print("------------------")

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list
print(my_list, new_list, sep='\n')
new_list[2] = 555
print(my_list, new_list, sep='\n')

print("------------------")

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
new_list = my_list.copy()
print(my_list, new_list, sep='\n')
my_list[2] = 555
print(my_list, new_list, sep='\n')

print("------------------")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = matrix.copy()
print(matrix, new_m, sep='\n')
matrix[0][1] = 555
print(matrix, new_m, sep='\n')

print("------------------")

import copy

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_m = copy.deepcopy(matrix)
print(matrix, new_m, sep='\n')
matrix[0][1] = 555
print(matrix, new_m, sep='\n')

print("------------------")

my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(len(my_list))
print(len(matrix))
print(len(matrix[1]))

print("------------------")

text = 'Hello world!'
print(text[6])
print(text[3:7])

print("------------------")

new_txt = text.replace('l', 'L', 2)
print(text, new_txt, sep='\n')

print("------------------")

text = 'Hello world!'
print(text[::-1])

print("------------------")

name = 'Alex'
age = 12
text = 'Меня зовут %s и мне %d лет' % (name, age)
print(text)

print("------------------")

name = 'Alex'
age = 12
text = 'Меня зовут {} и мне {} лет'.format(name, age)
print(text)

print("------------------")

name = 'Alex'
age = 12
text = f'Меня зовут {name} и мне {age} лет'
print(text)

print("------------------")

pi = 3.1415
print(f'Число Пи с точностью два знака: {pi:.2f}')
data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
for item in data:
    print(f'data = {item:>10}')

num = 2 * pi * data[1]
print(f'{num = :_}')

print("------------------")

link = 'https://habr.com/ru/users/dzhoker1/posts/'
urls = link.split('/')
print(urls)
#a, b, c = input('Введите 3 числа через пробел: ').split()
print(c, b, a)

print("------------------")

#a, b, c, *_ = input('Введите не менее трёх чисел через пробел:').split()

print("------------------")

data = ['https:',
'posts']
url = '/'.join(data)
print(url)

print("------------------")

text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

print("------------------")

text = 'Однажды в студёную зимнюю пору'
print(text.startswith('Однажды'))
print(text.endswith('зимнюю', 0, -5))

print("------------------")

a = ()
b1 = 1,
b2 = (1,)
c1 = 1, 2, 3,
c2 = (1, 2, 3)
d = tuple(range(3))
print(a, b1, b2, c1, c2, d, sep='\n')

print("------------------")

my_tuple = (2, 4, 6, 2, 8, 10, 12, 14, 16, 18)
print(my_tuple[2:6:2])
print(my_tuple[-3])
print(my_tuple.count(2))
print(f'{my_tuple = }')
print(my_tuple.index(2, 2))
print(type('text',))

print("------------------")

a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
b = dict(one=42, two=3.14, ten='Hello world!')
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])
print(a == b == c)

print("------------------")

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
my_dict['ten'] = 10
print(my_dict)

print("------------------")

TEN = 'ten'
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict['two'])
print(my_dict[TEN])
#print(my_dict[1]) # KeyError: 1

print("------------------")

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.get('two'))
print(my_dict.get('five'))
print(my_dict.get('five', 5))
print(my_dict.get('ten', 5))

print("------------------")

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.setdefault('five')
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.setdefault('six', 6)
print(f'{eggs = }\t{my_dict=}')
new_spam = my_dict.setdefault('two')
print(f'{new_spam=}\t{my_dict=}')
new_eggs = my_dict.setdefault('one', 1_000)
print(f'{new_eggs=}\t{my_dict=}')

print("------------------")

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
print(my_dict.keys())
for key in my_dict.keys():
    print(key)

print("------------------")

my_dict = {'one': 1,'two': 2,'three': 3,'four': 4,'ten': 10}
print(my_dict.values())
for value in my_dict.values():
    print(value)

print("------------------")

my_dict = {'one': 1,'two': 2,'three': 3,'four': 4,'ten': 10}
print(my_dict.items())
for tuple_data in my_dict.items():
    print(tuple_data)
for key, value in my_dict.items():
    print(f'{key = } value before 100 - {100 - value}')

print("------------------")

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.popitem()
print(f'{spam = }\t{my_dict=}')
eggs = my_dict.popitem()
print(f'{eggs = }\t{my_dict=}')

print("------------------")

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
spam = my_dict.pop('two')
print(f'{spam = }\t{my_dict=}')
#err = my_dict.pop('six') # KeyError: 'six'
#err = my_dict.pop() # TypeError: pop expected at least 1
#argument, got 0

print("------------------")

my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
my_dict.update(dict(six=6))
print(my_dict)
my_dict.update(dict([('five', 5), ('two', 42)]))
print(my_dict)

print("------------------")

my_set = {1, 2, 3, 4, 2, 5, 6, 7}
print(my_set)
my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,))
print(my_f_set)
#not_set = {1, 2, 3, 4, 2, 5, 6, 7, ['a','b']} # TypeError: unhashable type: 'list'

print("------------------")

my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.add(9)
print(my_set)
my_set.add(7)
print(my_set)
#my_set.add(9, 10) # TypeError: set.add() takes exactly one
#argument (2 given)
my_set.add((9, 10))
print(my_set)

print("------------------")

my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.remove(5)
print(my_set)
#my_set.remove(10) # KeyError: 10

print("------------------")

my_set = {3, 4, 2, 5, 6, 1, 7}
my_set.discard(5)
print(my_set)
my_set.discard(10)

print("------------------")

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.intersection(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')

print("------------------")

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set & other_set
print(f'{my_set = }\n{other_set = }\n{new_set = }')

print("------------------")

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.union(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')
new_set_2 = my_set | other_set
print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')

print("------------------")

my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.difference(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = }')
new_set_2 = my_set - other_set
print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')

print("------------------")

my_set = {3, 4, 2, 5, 6, 1, 7}
print(42 in my_set)

print("------------------")
"""
Условие
1. Решить задачи, которые не успели решить на семинаре.
2. Дан список повторяющихся элементов. Вернуть список с 
дублирующимися элементами. В результирующем списке не 
должно быть дубликатов.
3. В большой текстовой строке подсчитать количество 
встречаемых слов и вернуть 10 самых частых. Не учитывать 
знаки препинания и регистр символов. За основу возьмите 
любую статью из википедии или из документации к языку.
4. Создайте словарь со списком вещей для похода в качестве 
ключа и их массой в качестве значения. Определите какие вещи 
влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант.*Верните все 
возможные варианты комплектации рюкзака.
"""

#Задание 2
from random import randint
from collections import Counter
import collections

random_list=[]
for i in range(20):
    random_list.append(randint(1,5))
print(random_list)

print([item for item, count in collections.Counter(random_list).items() if count > 1])

print("------------------")

#Задание 3 В большой текстовой строке подсчитать количество 
#встречаемых слов и вернуть 10 самых частых. Не учитывать 
#знаки препинания и регистр символов. За основу возьмите 
#любую статью из википедии или из документации к языку

text = "Ардатов — рабочий посёлок в Нижегородской области России. Административный центр Ардатовского муниципального округа. Расположен в 165 километрах к юго-западу от Нижнего Новгорода и в 430 километрах к востоку от Москвы. Ближайшая железнодорожная станция — Мухтолово — находится примерно в 27 километрах к северу.Стоит на месте предположительно существовавшего с XIII века булгарского таборного городища, а затем — ордынского укреплённого поселения. После присоединения этой территории к Русскому государству в 1552 году — ясачное село (первое упоминание в 1578 году). Население сперва смешанное русско-мордовское, а к концу XVII — началу XVIII века — полностью русское. С 1779 по 1923 год — уездный город, с 1925 года — село, с 1929 года — районный центр, с 1959 года — рабочий посёлок. По состоянию на 2022 год, население Ардатова составляло 9768 человек. Вплоть до середины XX века основу экономики составляло сельское хозяйство, в дальнейшем наметилась тенденция к бо́льшей роли промышленности. На территории посёлка находятся 2 техникума, 2 общеобразовательные средних школы, 4 детских сада, дом культуры, 2 библиотеки, краеведческий музей, детская школа искусств, центральная районная больница, физкультурно-оздоровительный комплекс. С 1930 года выходит районная газета. Вплоть до начала XX века Ардатов имел большое религиозное значение — на его территории располагались Покровский женский монастырь, 3 церкви и несколько часовен. Все они были закрыты в советское время. С 1990 года началось восстановление некоторых церквей и строительство новых, с 2012 года посёлок является центром Ардатовского благочиния Выксунской епархии Русской православной церкви. Однако по состоянию на 2024 год территория бывшего монастыря занята женской исправительной колонией. Ардатов не имеет большого туристического потенциала, но на его территории находятся более 20 объектов, признанных памятниками истории и культуры регионального значения, а его центральная часть объявлена охранной зоной."
a = text.lower()
b = a.split()
duplicate_elements = {}

for item in b:
    if item in duplicate_elements:
        duplicate_elements[item] += 1
    else: 
        duplicate_elements[item] = 1

print(duplicate_elements)

#4. Создайте словарь со списком вещей для похода в качестве 
#ключа и их массой в качестве значения. Определите какие вещи 
#влезут в рюкзак передав его максимальную грузоподъёмность. 
#Достаточно вернуть один допустимый вариант.*Верните все 
#возможные варианты комплектации рюкзака.

from itertools import permutations
from itertools import combinations

items = [('knife', 3), ('matches', 1), ('cup', 5), ('sunbed', 15), ('first_aid_kid', 4)]
max_w = 20
print(max(filter(lambda x: sum(list(zip(*x))[0]) <= max_w, (v for r in range(1, len(items)) for v in combinations(filter(lambda x: x[0] <= max_w, items), r))), key=lambda x: sum(list(zip(*x))[1])))

"""
max_degree = max_weight_backpack / min([x[1] for x in backpack])
result = []

for degree in range(0, max_degree + 1):
    for ss in permutations(backpack * degree, degree):
        if ss not in result and sum(map(lambda y: y[1], list(ss))) == 20:
            result.append(ss)
for i in result:
    print(" + ".join(map(lambda z: z[0], list(i))))
    """