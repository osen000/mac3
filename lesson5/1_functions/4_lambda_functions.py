# Применим lambda для сортировки массива
names = [
    "Генадий Букин",
    "Тим Эпл",
    "Аркадий Волож",
    "Билл Гейтс",
    "Илон Маск",
    "Игорь Николаев",
    "Джеф Безос",
    "Майк Тайсон"
]

# 1. Сортируем по имени
# 2. Сортируем по фамилии

def get_surname(name):
    return name.split(" ")[1]

sorted_names = sorted(names, key=get_surname)

print(sorted_names)
