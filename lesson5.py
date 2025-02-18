import os

def split_file_path(file_path):
    path, file_name = os.path.split(file_path)
    name, extension = os.path.splitext(file_name)
    return (path, name, extension)

result = split_file_path('/home/user/document.txt')
print(result)

def calculate_bonus(names, rates, bonuses):
    return {name: rate * (float(bonus[:-1]) / 100) for name, rate, bonus in zip(names, rates, bonuses)}

names = ["Alice", "Bob", "Charlie"]
rates = [1000, 1500, 2000]
bonuses = ["10.25%", "5%", "8.5%"]
result = calculate_bonus(names, rates, bonuses)
print(result)

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen))