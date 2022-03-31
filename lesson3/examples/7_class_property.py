class Vehicle:
    _wheels = None
    __engine_status = "Off"

    def __init__(self, brand, model, wheels):
        self.brand = brand
        self.model = model
        self._wheels = wheels

    def set_wheels(self, amount):
        if amount > 0:
            self._wheels = amount

    def get_engine_status(self):
        return self.__engine_status

    @property
    def engine_status(self):
        return self.__engine_status


v1 = Vehicle("1", "2", 4)
v2 = Vehicle("1", "2", 4)

print(v1.engine_status)

v2._wheels = 10

print(v1._wheels)
