import inspect


# Объявление функции
def base_function():
    pass  # Тело функции


def advanced_function(arg):  # Имя функции
    """ Докстринга функции """
    return arg  # Возвращаемое значение


# Сигнатура функции - в общем понимании это совокупность имени, кол-ва и порядка аргументов, возвращаемого значения.

print("=== Функция является объектом ===")
print(dir(advanced_function))
print("name:", advanced_function.__name__)
print("code:", advanced_function.__code__)
print("code:", advanced_function.__doc__)
print("type:", type(advanced_function))

print("=== Использование функции как объекта первого класса ===")
# Хранить в структурах данных
my_functions = [base_function, advanced_function, 10, None]
print(my_functions)

# Присваивать переменным
my_arg = advanced_function
my_arg(10)

# Передавать в качестве аргумента другим функциям
advanced_function(base_function)

# Возвращать из функций
result = advanced_function(base_function)
result()

# Вызов при возвращении
advanced_function(base_function)()

print("=== Возвращаемые значения ===")


def example1():
    print('example1')


def example2():
    return "example2"
