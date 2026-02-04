from car import Car
# Creating objects (instances of class)

car1 = Car("Toyota", "Corolla","red",False)
car2 = Car("Honda", "Civic","blue",True)

print(car1.brand)
print(car1.model)

car1.stop()
car1.describe()