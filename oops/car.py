class Car:
    # Constructor (special method to initialize object)
    def __init__(self, brand, model,color,for_sale):
        self.brand = brand   # attribute
        self.model = model   # attribute
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print("you drive the car")

    def stop(self):
        print(f"you stop the {self.model}")

    def describe(self):
        print(f"{self.brand},{self.color},{self.model}")