"""
What is a Module?
modules are the (.py) files ,that contains set of functions you want to include in your program.
A module is simply a file containing Python code (functions, classes, or variables).

It helps organize code into separate files instead of writing everything in one place.

Python comes with many built-in modules (like math, random, os) and you can also create your own.

📝 Why Use Modules?
Reusability → Write once, use in multiple programs.

Organization → Keep code clean and structured.

Namespace management → Avoid variable/function name conflicts.

Built-in power → Access thousands of ready-made functions.

example of modules are: import math ,import random etc.

"""
#TYPES OF MODULES
#BUILT-IN MODULES

#DATETIME module
# import datetime
# x = datetime.datetime.now() #give current date time
# print(x)
# #########
# y = datetime.datetime(1997,10,14) #(year,month,date)
# print(y.strftime("%A"))
#"%A" = GIVE FULL NAME OF DAY ,TUESDAY
#"%a" = give short form ,tue
#"%B" = GIVE THE MONTH ,OCTOBER
#"%M" = GIVE NUMERIC VALUE OF MONTH,10
#"%Y" = GIVE full YEAR NAME 1997
#"%y" = give only year ,97.


###############################################

#RANDOM MODULE
# import random
# x = random.randint(1,10) #give random number b\w 1 to 10
# print(x) 
#for string 
# l = ["heads","tails"]
# x= random.choice(l)
# print(x)


###############################################
#MATH MODULE

# import math
# x = max(13,6,7,89,98,12222)
# print("the maximum value is: ",x)
# y =min(3,5,6,7,8,1)
# print ("the minimum value is: ",y) 
################for power####
# a = pow(2,4)
# print(a)
#for sqrt number 
# b = math.sqrt(256)
# print(b)
############for absolute value of a number
# c = abs(-12.3*4)
# print (c)

###########################################
#FLOOR AND CEIL FUNCTION
# import math
# a = 2.5
# b =34.6  
# print("Floor of a :", math.floor(a)) #give 2
# print("Ceil of  b  :", math.ceil(b)) #give 35 
