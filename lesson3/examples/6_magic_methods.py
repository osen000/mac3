class Beauty:

    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return "= Beauty:{} =".format(self.amount)

    def __str__(self):
        return "B*E*A*U*T*Y:{}".format(self.amount)

    def __add__(self, other):
        if not isinstance(other, Beauty):
            raise ValueError("Cant be summed")
        return self.amount + other.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __call__(self, *args):
        return str(self) + " got args " + str(args)


b1 = Beauty(100)
b2 = Beauty(100)

print(b1.__add__(b2))

#
# print(b1("BOOOOO"))
