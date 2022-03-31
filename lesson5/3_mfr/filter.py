def is_digit(x):
    return str(x).isnumeric()
    # return isinstance(x, int)
    # return isinstance(x, float)
    # return isinstance(x, object)


s_list = [None, [], "2", 2, 1.0, int, str, "B", "b"]

# Применение lambda функций так же возможно
filtered_s = filter(lambda item: str(item).isnumeric(), s_list)

filtered = []
for el in s_list:
    if is_digit(el):
        filtered.append(el)
print(filtered)