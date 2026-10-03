# Генератор парних чисел від 0 до N
def even_numbers(n):
    for num in range(0, n + 1, 2):
        yield num
# Генератор послідовності Фібоначчі до N
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
# Ітератор для зворотного виведення елементів списку
class ReverseListIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]
# Ітератор, який повертає всі парні числа від 0 до N
class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 2
        return value
# Декоратор, який логує аргументи та результат функції
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Виклик функції: {func.__name__}")
        print(f"Аргументи: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper
# Декоратор, який перехоплює та обробляє винятки
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print(f"Сталася помилка: {error}")
            return None
    return wrapper
