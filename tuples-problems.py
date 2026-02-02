#################################################
# Tuple Operations Program

# # Step 1: Create tuples
# heroes = ("Superman", "Batman", "Ironman", "Spiderman")
# numbers = (10, 20, 30, 40, 50, 60)
# students = (("john", 21), ("Amit", 22), ("Riya", 20))

# print("=== Original Tuples ===")
# print("Heroes:", heroes)
# print("Numbers:", numbers)
# print("Students:", students)
# print("-" * 40)

# # Step 2: Slicing examples
# print("First two heroes:", heroes[:2])
# print("Last three numbers:", numbers[-3:])
# print("Reverse heroes:", heroes[::-1])
# print("-" * 40)

# # Step 3: Iteration examples
# print("Iterating heroes with for loop:")
# for hero in heroes:
#     print(hero)

# print("\nIterating heroes with index:")
# for i in range(len(heroes)):
#     print(f"Index {i}: {heroes[i]}")

# print("\nIterating heroes with enumerate:")
# for index, hero in enumerate(heroes):
#     print(f"{index} → {hero}")
# print("-" * 40)

# # Step 4: Tuple functions
# marks = (85, 90, 75, 90, 95)
# print("Marks tuple:", marks)
# print("Count of 90:", marks.count(90))
# print("Index of 75:", marks.index(75))
# print("Length of marks tuple:", len(marks))
# print("-" * 40)

# # Step 5: Nested tuple iteration
# print("Student records:")
# for name, age in students:
#     print(f"Name: {name}, Age: {age}")
# print("-" * 40)

# # Step 6: Tuple unpacking
# point = (10, 20)
# x, y = point
# print("Tuple unpacking example:")
# print("x =", x, "y =", y)
