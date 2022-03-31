class Car:
    engine_status = "Off"

    def __init__(self, brand, model, wheels):
        """Class constructor"""
        self.brand = brand
        self.model = model
        self.wheels = wheels

    def start_engine(self):
        self.engine_status = "On"
        print(f"Engine of {self.brand} {self.model} started.")

    def stop_engine(self):
        self.engine_status = "On"
        print(f"Engine of {self.brand} {self.model} stopped.")


toyota_camry = Car(brand="Toyota", model="Camry", wheels=4)
honda_trio = Car(brand="Honda", model="Civic", wheels=3)
