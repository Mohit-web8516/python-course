###########################
#return statement
# def hello():
#     return ("Hello world")

# print(hello())
##########################
# def add(a , b):
#     return ("The addition  of two numbers is ",a + b)

# print(add(12,4))

########################################
#RECURSION == MEANS A FUNCTION CAN CALL ITSELF.

# def hello():
#     print("hello")
#     return hello()

# print(hello())  

#################################
#factorial series
# def factorial(n):
#     if n == 0 or n == 1:   # base case
#         return 1
#     else:
#         return n * factorial(n - 1)   # recursive case

# print("Factorial of 4:", factorial(4))

###################################
#fabonacci sequence

# def fibonacci(n):
#     if n == 0:   # base case
#         return 0
#     elif n == 1: # base case
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)   # recursive case

# print("Fibonacci(6):", fibonacci(6))

########################################
#LAMBDA FUNCTION == A lambda function is a small, anonymous function (no name).
# a = lambda b:b*5
# print(a(4))
#####################
# x = lambda a,b,c: (a+b)*c
# print(x(3,7,2))

###################################
#LOCAL VARIABLE == DECLARED INSIDE A FUNCTION
#ACCESSIBLE ONLY WITHIN THAT FUNCTION

# x = 24 
# print("first variables x ", x)
# def hello ():
#     x = 25
#     return x

# print (hello())
# print(x)

################################

# def my_function():
#     x = 10   # local variable
#     print("Inside function:", x)

# my_function() # print(x)  # Error: x is not defined outside the function

#####################################
#GLOBAL VARIABLE == DECLARED OUTSIDE ALL FUNCTIONS.
# ACCESSIBLE THROUGHOUT THE PROGRAM .

# x = 24 
# print("first variables x ", x)
# def hello ():
#     global x
#     x = 25
#     return x

# print (hello())
# print(x)

#####################################
# y = 20   # global variable

# def my_function():
#     print("Inside function:", y)   # can access global variable

# my_function()
# print("Outside function:", y)
