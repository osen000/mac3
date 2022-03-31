def square_root(x):
    """квадратный корень"""
    return x ** 0.5


def square(x):
    """Возведение в квадрат"""
    return int(x ** 2)


some_range = range(10)

result = map(square_root, some_range)
result = map(square, result)

print(list(result))
