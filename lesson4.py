a = 42
print(type(a), id(a))
print(type(id))

print("------------------")

very_bad_programming_style = sum
print(very_bad_programming_style([1, 2, 3]))

print("------------------")

def quadratic_equations(a: int | float, b: int | float, c: int |
float) -> tuple[float, float] | float | str:
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        return -b / (2 * a)
    else:
        return 'Нет решений'

print(quadratic_equations(2, -3, -9))

print("------------------")

def no_mutable(a: int) -> int:
    a += 1
    print(f'In func {a = }') # Для демонстрации работы, но не для привычки принтить из функции
    return a

a = 42
print(f'In main {a = }')
z = no_mutable(a)
print(f'{a = }\t{z = }')

print("------------------")

def mutable(data: list[int]) -> list[int]:
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'In func {data = }') # Для демонстрации работы, но не для привычки принтить из функции
    return data
my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = mutable(my_list)
print(f'{my_list = }\t{new_list = }')

print("------------------")

def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None

print("------------------")

def no_return(data: list[int]):
    for i, item in enumerate(data):
        data[i] = item + 1
    print(f'In func {data = }') # Для демонстрации работы, но не для привычки принтить из функции

my_list = [2, 4, 6, 8]
print(f'In main {my_list = }')
new_list = no_return(my_list)
print(f'{my_list = }\t{new_list = }')

print("------------------")

def quadratic_equations(a, b = 0, c = 0):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    
print(quadratic_equations(2, -9))

print("------------------")

def from_one_to_n(n, data=[]):
    for i in range(1, n + 1):
        data.append(i)
    return data

new_list = from_one_to_n(5)
print(f'{new_list = }')
other_list = from_one_to_n(7)
print(f'{other_list = }')

print("------------------")

def from_one_to_n(n, data = None):
    if data is None:
        data = []
    for i in range(1, n + 1):
        data.append(i)
    return data

print("------------------")

def standard_arg(arg):
    print(arg) # Принтим для примера, а не для привычки

standard_arg(42)
standard_arg(arg=42)

print("------------------")

def pos_only_arg(arg, /):
    print(arg) # Принтим для примера, а не для привычки

pos_only_arg(42)
#pos_only_arg(arg=42) # TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

print("------------------")

def kwd_only_arg(*, arg):
    print(arg) # Принтим для примера, а не для привычки

#kwd_only_arg(42)
kwd_only_arg(arg=42)

print("------------------")

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only) # Принтим для примера, а не для привычки

#combined_example(1, 2, 3) # TypeError: combined_example() takes2 positional arguments but 3 were given
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
#combined_example(pos_only=1, standard=2, kwd_only=3) #TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'

print("------------------")

def triangulation(*, x, y, z):
    pass

triangulation(y=5, z=2, x=11)

print("------------------")

def mean(args):
    return sum(args) / len(args)

print(mean([1, 2, 9]))
#print(mean(1, 2, 3)) # TypeError: mean() takes 1 positional argument but 3 were given

print("------------------")

def mean(*args):
    return sum(args) / len(args)

print(mean(*[1, 2, 3]))
print(mean(1, 2, 3))

print("------------------")

def school_print(**kwargs):
    for key, value in kwargs.items():
        print(f'По предмету "{key}" получена оценка {value}')
school_print(химия=5, физика=4, математика=5, физра=5)

print("------------------")

def func(y: int) -> int:
    x = 100
    print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
    return y + 1

x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')

print("------------------")

def func(y: int) -> int:
    global x
    x += 100
    print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
    return y + 1

x = 42
print(f'In main {x = }')
z = func(x)
print(f'{x = }\t{z = }')

print("------------------")

def main(a):
    x = 1
    def func(y):
        nonlocal x
        x += 100
        print(f'In func {x = }') # Для демонстрации работы, ноне для привычки принтить из функции
        return y + 1
    return x + func(a)

x = 42
print(f'In main {x = }')
z = main(x)
print(f'{x = }\t{z = }')

print("------------------")

LIMIT = 1_000
def func(x, y):
    result = x ** y % LIMIT
    return result

print(func(42, 73))

print("------------------")

def add_two_def(a, b):
    return a + b

add_two_lambda = lambda a, b: a + b

print(add_two_def(42, 3.14))
print(add_two_lambda(42, 3.14))

print("------------------")

my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
s_key = sorted(my_dict.items())
s_value = sorted(my_dict.items(), key=lambda x: x[1])
print(f'{s_key = }\n{s_value = }')

print("------------------")
"""
def max_before_hundred(*args): Return the maximum number not exceeding 100.
    m = float('-inf')
        for item in args:
            if m < item < 100:
            m = item
return m

print(max_before_hundred(-42, 73, 256, 0))
"""
print("------------------")

texts = ["Привет", "ЗДОРОВА", "привеТствую"]
res = map(lambda x: x.lower(), texts)
print(*res)

print("------------------")

numbers = [42, -73, 1024]
res = tuple(filter(lambda x: x > 0, numbers))
print(res)

print("------------------")

names = ["Иван", "Николай", "Пётр"]
salaries = [125_000, 96_000, 109_000]
awards = [0.1, 0.25, 0.13, 0.99]
for name, salary, award in zip(names, salaries, awards):
    print(f'{name} заработал {salary:.2f} денег и премию {salary
* award:.2f}')

print("------------------")

lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр", 109_000)]
print(max(lst_1, default='empty'))
print(max(*lst_2))
print(max(lst_3, key=lambda x: x[1]))

print("------------------")

lst_1 = []
lst_2 = [42, 256, 73]
lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр", 109_000)]
print(min(lst_1, default='empty'))
print(min(*lst_2))
print(min(lst_3, key=lambda x: x[1]))

print("------------------")

my_list = [42, 256, 73]
print(sum(my_list))
print(sum(my_list, start=1024))

print("------------------")

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

print("------------------")

numbers = [42, -73, 1024]
if all(map(lambda x: x > 0, numbers)):
    print('Все элементы положительные')
else:
    print('В последовательности есть отрицательные и/или нулевые элементы')

print("------------------")

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

print("------------------")

numbers = [42, -73, 1024]
if any(map(lambda x: x > 0, numbers)):
    print('Хотя бы один элемент положительный')
else:
    print('Все элементы не больше нуля')

print("------------------")

print(chr(97))
print(chr(1105))
print(chr(128519))

print("------------------")

SIZE = 10
def func(a, b, c):
    x = a + b
    print(locals())
    z = x + c
    return z

func(1, 2, 3)

print("------------------")

x = 42
glob_dict = globals()
glob_dict['x'] = 73
print(x)

print("------------------")

"""
Условие
1. Напишите функцию для транспонирования матрицы
2. Напишите функцию принимающую на вход только ключевые 
параметры и возвращающую словарь, где ключ — значение 
переданного аргумента, а значение — имя аргумента. Если 
ключ не хешируем, используйте его строковое представление.
3. Возьмите задачу о банкомате из семинара 2. Разбейте её 
на отдельные операции — функции. Дополнительно сохраняйте 
все операции поступления и снятия средств в список.
"""
print("------------------")


def trans_func(a, b, c, d, e, f):
    matrix = [[a, b, c], [d, e, f]]
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j] 
        for row in matrix:
            print(row)
        print('----------')
        for row in transposed:
            print(row)
        print('----------')
    print(matrix)
    print(transposed)

trans_func(1, 2, 3, 4, 5, 6)
        
print("------------------")
"""
def create_dict(*kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result

result = create_dict(a = 1, b=2, c=[3, 4])

print(result)
"""
print("------------------")



print("------------------")