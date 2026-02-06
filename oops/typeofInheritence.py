#multiple inheritance = inherit from more than one parent class
                            # C(A,B)
class Animal:
    def __init__ (self,name):
        self.name = name
       
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit (Prey):
    pass

class Hawk (Predator):
    pass

class Fish (Prey,Predator):
    pass 

rabbit = Rabbit("bugs")
hawk = Hawk("tony")
fish = Fish("nemo")

hawk.sleep()


# class Father:
#     def skill(self):
#         print("Father: Driving")

# class Mother:
#     def skill(self):
#         print("Mother: Cooking")

# class Child(Father, Mother):
#     def hobby(self):
#         print("Child: Painting")

# c = Child()
# c.skill()   # Which skill will be called?
# c.hobby()

# #ANOTHER EXAMPLE OF MULTIPLE INHERITANCE
# class A:
#     def methodA(self):
#         print("This is from class A")

# class B:
#     def methodB(self):
#         print("This is from class B")

# # Child inherits from both A and B
# class C(A, B):
#     def methodC(self):
#         print("This is from class C")

# # Using the child class
# obj = C()
# obj.methodA()   # inherited from A
# obj.methodB()   # inherited from B
# obj.methodC()   # defined in C






























#multilevel inheritance = inherit from a parent which inherits from another parent
#C(B) <- B(A) <-A