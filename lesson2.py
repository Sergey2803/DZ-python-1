#LECTION #2

data = 42
print(isinstance(data, int))

print ("-----------")

data = True
print(isinstance(data, int))

print ("-----------")

data = 3.14
print(isinstance(data, (int, float, complex)))

print ("-----------")

num = 2 + 2 * 2
digit = 36 / 6
print (num == digit)
print (num is digit)

print ("-----------")

a = 5
print(a, id(a))
a += 1
print(a, id(a))

print ("-----------")

txt = "Hello World"
print(txt, id(txt))
txt = txt.replace(" ", "_")
print(txt, id(txt))

print ("-----------")

a = c = 2
b = 3
print(a, id(a), b, id(b), c, id(c))
a = b + c
print(a, id(a), b, id(b), c, id(c))

print ("-----------")

x = 42
y = "text"
z = 3.1415
print(hash(x), hash(y), hash(z))
#my_list = [x, y, z]
#print(hash(my_list))

print ("-----------")

a: int = 42
#b: float = float(input("Введите число: "))
a = a / b

print ("-----------")

def my_func(data: list[int, float]) -> float:
    res = sum(data) / len(data)
    return res

print(my_func([2, 5.5, 15, 8.0, 13.74]))

print ("-----------")

print("Hello world!".__doc__)
print(str.__doc__)

print ("-----------")

print(dir('Hello World!'))

print ("-----------")

#help(str)

import sys

STEP = 2 ** 16
num = 1
for _ in range (30):
    print(sys.getsizeof(num), num)
    num *= STEP

print ("-----------")

num = 2 ** 16 - 1
b = bin(num)
o = oct(num)
h = hex(num)

print(b, o, h)

print ("-----------")

import math
import decimal
import fractions

pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
print(pi)
num = decimal.Decimal(1) / decimal.Decimal(3)
print(num)

print ("-----------")

decimal.getcontext().prec = 120
science = 2 * pi * decimal.Decimal(23.452346) ** 2
print(science)

print ("-----------")

f1 = fractions.Fraction(1, 3)
print(f1)
f2 = fractions.Fraction(3, 5)
print(f2)
print(f1 * f2)

print ("-----------")

a = complex(2, 3)
b = complex('2+3j')
print(a, b, a == b, sep='\n')

print ("-----------")

""" DZ
Условие
1. Решить задачи, которые не успели решить на семинаре.
2. Напишите программу, которая получает целое число и возвращает 
его шестнадцатеричное строковое представление. Функцию hex используйте 
для проверки своего результата.
3. Напишите программу, которая принимает две строки вида “a/b” - дробь 
с числителем и знаменателем. Программа должна возвращать сумму и 
произведение* дробей. Для проверки своего кода используйте модуль fractions
"""

a = int(input("Введите целое число: "))
print(hex(a))


a = int(input("Введите числитель первой дроби: "), base = 30)
b = int(input("Введите знаменатель первой дроби: "), base = 30)
c = int(input("Введите числитель первой дроби: "), base = 30)
d = int(input("Введите знаменатель первой дроби: "), base = 30)
f1 = fractions.Fraction(a, b)
f2 = fractions.Fraction(c, d)
print(f1 * f2)
