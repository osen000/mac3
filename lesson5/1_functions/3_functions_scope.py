A = 1

# example 1
def change():
    A = A + 5
    print(A)

change()


# example 2
def change():
    global A
    A = A + 5
    print(A)

change()

print("After calling change() GLOBAL_A =", A)
