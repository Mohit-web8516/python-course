#write a function to find maximum of three numbers in python.
# def maximum_num(a,b,c):
#     if a > b and a > c:
#         print (a,"is the maximum number")
#     elif b > a and b > c:
#         print (b,"is the maximum number")
#     else:
#         print(c,"is the maximum number")

# maximum_num(23,56,89)
######################################
#######second method
# def max_of_three(a, b, c):
#     return max(a, b, c)

# print("Maximum:", max_of_three(10, 25, 15))

#write a python function to create and print a list where the values are square of numbers between 1 and 30.
# def create_list():
#     l = []
#     for i in range(1,31):
#         l.append(i**2)

#     return l

# print(create_list())

###############################################################

#write a python function that takes a number as a parameter and check if the number is prime or not.
# def prime_num(num):
#     if num == 1:
#         print("it is not a prime number")
#     if num == 2:
#         print("it is a prime number")
#     if num>2:
#      for i in range (2,num):
#         if num % i == 0:
#             print("it is not a prime number")
#             break
#     else:
#         print("it is a prime number")
# prime_num(11)
###############################################
#############################################

#write a python function to sum all the numbers in a list.
# def add(numbers):
#     total = 0
#     for i in numbers:
#         total = total + i
#     return (total)
# print("the sum of all the num is :",add([12,4,56,6,7,8]))

####method 2 using recursion
# def add(numbers):
#     if len(numbers) ==1:
#         return (numbers[0])
#     else:
#         return (numbers[0] + add(numbers[1:]))
# print(add( [1,2,4,5,6,7]))

################################################################
#write a python program to solve the fibonacci sequence using recursion
# def fibonacci(n):
#     if n == 0:   # base case
#         return 0
#     elif n == 1: # base case
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)   # recursive case

# # Print first 10 Fibonacci numbers
# for i in range(10):
#     print(fibonacci(i))
