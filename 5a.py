class Car:
    def __init__(self, brand, speed):  # Fixed method name: __init__
        self.brand = brand
        self.speed = speed

    def display(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} km/h")

def create_car():  # Moved this function outside the class
    car1 = Car("THAR", 210)
    return car1

my_car = create_car()
my_car.display()

