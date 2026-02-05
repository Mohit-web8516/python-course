# Parent/Base Class: The class whose properties and methods are inherited.

# Child/Derived Class: The class that inherits from the parent

#INHERIRENCE
#ALLOWS A CLASS TO INHERIT ATTRIBUTES AND METHODS FROM ANOTHER CLASS HELPS
#WITH CODE REUSABILITY AND EXTENSIBILITY CLASS CHILD(PARENT)
class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass

class Cat(Animal):
    pass


class Mouse(Animal):
    pass

dog = Dog("scooby")
cat = Cat("garfield")
mouse = Mouse("mickey")


print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()