import json
import csv


def get_csv():
    with open("books.csv", "r") as fileHeader:
        headers = csv.DictReader(fileHeader).fieldnames

    with open("books.csv", "r") as file:
        reader = csv.DictReader(file)
        if 'Publisher' in headers:
            books_ls = []
            for row in reader:
                del row['Publisher']
                books_ls.append(row)
        else:
            print("Вероятно структура books.csv была изменена")

        books = []
        for book in books_ls:
            new_books = ({'title': book['Title'], 'author': book['Author'], 'genre': book['Genre'],
                          'pages': book['Pages']})
            books.append(new_books)
        return books


def get_json():
    with open("users.json", "r") as f:
        users_file = json.load(f)
        users_ls = []
        for param in users_file:
            users = ({'name': param['name'], 'gender': param['gender'], 'address': param['address'],
                      'age': param['age'], 'books': []})
            users_ls.append(users)

        return users_ls


def union_file():
    books = get_csv()
    users = get_json()
    while len(books) > 0:
        for param in users:
            if len(books) > 0:
                book_row = books.pop()
                param.get('books').append(book_row)

    return users


def record_file():
    with open('result.json', "w") as file:
        users = union_file()
        json.dump(users, file, indent=4)


record_file()
