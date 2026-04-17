# # Python Revision Program
# def variables_demo():
#     x = 10
#     y = 3.5
#     name = "Mohit"
#     print("Integer:", x)
#     print("Float:", y)
#     print("String:", name)

# def loops_demo():
#     print("For loop example:")
#     for i in range(1, 6):
#         print(i, end=" ")
#     print("\nWhile loop example:")
#     count = 1
#     while count <= 5:
#         print(count, end=" ")
#         count += 1

# def functions_demo():
#     def greet(name):
#         return f"Hello, {name}!"
#     print(greet("Mohit"))

# def lists_demo():
#     fruits = ["apple", "banana", "cherry"]
#     print("Original list:", fruits)
#     fruits.append("mango")
#     print("After append:", fruits)
#     fruits.remove("banana")
#     print("After remove:", fruits)

# def file_demo():
#     with open("revision.txt", "w") as f:
#         f.write("This is a sample file.\n")
#     with open("revision.txt", "r") as f:
#         print("File content:")
#         print(f.read())

# def main():
#     while True:
#         print("\n--- Python Revision Menu ---")
#         print("1. Variables")
#         print("2. Loops")
#         print("3. Functions")
#         print("4. Lists")
#         print("5. File Handling")
#         print("6. Exit")
        
#         choice = input("Enter your choice: ")
        
#         if choice == "1":
#             variables_demo()
#         elif choice == "2":
#             loops_demo()
#         elif choice == "3":
#             functions_demo()
#         elif choice == "4":
#             lists_demo()
#         elif choice == "5":
#             file_demo()
#         elif choice == "6":
#             print("Exiting... Happy Revising!")
#             break
#         else:
#             print("Invalid choice, try again.")

# if __name__ == "__main__":
#     main()
# #########################################################
# # Extended Python Revision Program

# # --- OOP Demo ---
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         return f"{self.name} makes a sound."

# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} barks!"

# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} meows!"

# def oop_demo():
#     dog = Dog("Tommy")
#     cat = Cat("Kitty")
#     print(dog.speak())
#     print(cat.speak())

# # --- Exception Handling Demo ---
# def exception_demo():
#     try:
#         num = int(input("Enter a number: "))
#         print("Reciprocal is:", 1/num)
#     except ValueError:
#         print("Invalid input! Please enter a number.")
#     except ZeroDivisionError:
#         print("Cannot divide by zero!")

# # --- Multithreading Demo ---
# import threading
# import time

# def print_numbers():
#     for i in range(1, 6):
#         print("Number:", i)
#         time.sleep(1)

# def print_letters():
#     for ch in ['A', 'B', 'C', 'D', 'E']:
#         print("Letter:", ch)
#         time.sleep(1)

# def threading_demo():
#     t1 = threading.Thread(target=print_numbers)
#     t2 = threading.Thread(target=print_letters)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print("Threads finished execution.")

# # --- Main Menu ---
# def main():
#     while True:
#         print("\n--- Python Revision Menu ---")
#         print("1. Variables")
#         print("2. Loops")
#         print("3. Functions")
#         print("4. Lists")
#         print("5. File Handling")
#         print("6. OOP Concepts")
#         print("7. Exception Handling")
#         print("8. Multithreading")
#         print("9. Exit")
        
#         choice = input("Enter your choice: ")
        
#         if choice == "1":
#             variables_demo()
#         elif choice == "2":
#             loops_demo()
#         elif choice == "3":
#             functions_demo()
#         elif choice == "4":
#             lists_demo()
#         elif choice == "5":
#             file_demo()
#         elif choice == "6":
#             oop_demo()
#         elif choice == "7":
#             exception_demo()
#         elif choice == "8":
#             threading_demo()
#         elif choice == "9":
#             print("Exiting... Keep Revising!")
#             break
#         else:
#             print("Invalid choice, try again.")

# if __name__ == "__main__":
#     main()

########################################################
# Conditional Statements and Operators Demo

def conditional_demo():
    num = int(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

def operators_demo():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # Arithmetic Operators
    print("\n--- Arithmetic Operators ---")
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b if b != 0 else 'Division by zero error'}")
    print(f"{a} % {b} = {a % b if b != 0 else 'Modulo by zero error'}")

    # Relational Operators
    print("\n--- Relational Operators ---")
    print(f"{a} > {b} = {a > b}")
    print(f"{a} < {b} = {a < b}")
    print(f"{a} == {b} = {a == b}")
    print(f"{a} != {b} = {a != b}")

    # Logical Operators
    print("\n--- Logical Operators ---")
    print(f"(a > 0) and (b > 0) = {(a > 0) and (b > 0)}")
    print(f"(a > 0) or (b > 0) = {(a > 0) or (b > 0)}")
    print(f"not(a > 0) = {not(a > 0)}")

def main():
    while True:
        print("\n--- Conditional & Operators Menu ---")
        print("1. Conditional Statements")
        print("2. Operators")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            conditional_demo()
        elif choice == "2":
            operators_demo()
        elif choice == "3":
            print("Exiting... Keep practicing!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
