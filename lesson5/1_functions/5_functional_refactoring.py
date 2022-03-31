a = input("Input number a: ")
b = input("Input number b: ")

a = int(a)
b = int(b)

action = input("Input action [+, -, /, *]: ")

if action == "+":
    print(a + b)
elif action == "-":
    print(a - b)
elif action == "/":
    print(a / b)
else:
    print(a * b)
