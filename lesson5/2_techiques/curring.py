from functools import partial


# Каррирование (от англ. currying, иногда — карринг) — преобразование функции от многих аргументов в набор функций,
# каждая из которых является функцией от одного аргумента. По факту же просто от меньшего числа аргументов.

def money_transfer(client_from, client_to, amount, currency, pay_system):
    print(f"Transfer from: {client_from} to: {client_to} made for {amount} {currency} with {pay_system}")
MAX_AMOUNT = 150000


# Мы можем сделать так
def ruble_visa_transfer_for_test(client_from, client_to):
    return money_transfer(client_from, client_to, 0.1, "RUB", "VISA")


def ruble_visa_transfer_max_amount(client_from, client_to):
    return money_transfer(client_from, client_to, MAX_AMOUNT, "RUB", "VISA")


def one_euro_mastercard_transfer(client_from, client_to):
    return money_transfer(client_from, client_to, 1.00, "EUR", "MasterCard")


dollar_visa_transfer = partial(money_transfer, currency="USD", pay_system="VISA")
dollar_visa_transfer("Donald", "Joe", 100)
