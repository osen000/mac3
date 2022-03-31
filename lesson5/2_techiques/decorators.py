def some_stuff(func):

    def new():
        print("-------------")

    return new


@some_stuff
def say_hello():
    return "hello"


print(say_hello())
