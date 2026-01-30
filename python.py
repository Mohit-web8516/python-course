#starting with basic program
# print("hello world")
###########################################
# using multiple lines in print statement .

# print("""hello !
# how are you all ?
# this my first program!""")
#################################################
# by using \n for multiple line in print statement.

# print("its interesting to learn python \n its engaging and easy to understand \n you should learn python!")

#######################################################################
# comments in pyrthon

# by using "#" in a statement ,we can add some information for required program ,this is totally ingored by python while compiling

# for multiple line comments 
"""hello how are you today!"""
######################################################

# variables
# a = "hello world!"
# print(a)
# don't use "" while printing variable in ()
# givennum= "10"
# print(givennum)

# data types and user-input
# name = input("enter your name here: ")
# print(name)
#############################################################
# strings input
# name =input("enter name: ")
# age = int(input("enter age : "))
# age = float(input("enter your age : "))
# ex1 = eval(input("enter any expression : "))
# print(ex1)
##############################################
# TYPECASTING (converting one type of data type into other data type)
# name ="Mohit"
# print(type(name))
# num = 23
# print(type(num))
#############
# a = 23
# b = 21.4
# print(type(a))
# print(type(b))
# c = a + b
# print(type(c))
##############################################################
# conversion
############################################
# a = "23"
# b = 27.1
# print (type(a))
# print(type(b))
# a = float(a)
# print("After conversion ", type(a))
# c = a + b 
# print(type (c))
# c = int(c)
# print(type(c))
#############################################
"""problem solving"""
# question-1

# print("This is a Atul  \n he is 14 year old\n and live in his house hahahhaahha")
###################################################################
# question-2
# write a  program to swap two variable
# a = "Mohit"
# b = 25
# temp = a
# a = b
# b = temp
# print (temp)
##################################################
# method 2
# a = 24
# b = 45
#####left,right = right,left
# a,b = b,a
# print(b)
#####################################################
# question-3
# to convert a float into integer
# a = 12.4
# print(type (a))
# a = int((a))
# print(type(a))
# print(a)
###############################################################
# question -4
# take input from a student of ID card and print it in different lines.

# print("STUDENT IDENTITY  CARD")
# name = input("Enter your name : ")
# age= int(input("Enter your age : "))
# grade= input("Enter your grade : ")
# roll_no = input("Enter your roll no. : ")
# add = input ("Enter your address: ")
# college_name = input ("Enter your college name : ")
# print("name: ",name ) 
# print("age : " ,age)
# print("grade : ", grade)
# print("roll_no : ", roll_no)
# print("add: " ,add)
# print("college_name : ", college_name)
################################################################
# question-5
# write a program to take an user input as integer then convert it to float

# m = int(input("Enter your number here : ")) 
# print(m)
# print(type(m))
# m = float(m)
# print("After conversion ", m)
# print(type(m))
################################################
# OPERATORS AND OPERANDS 
############################################
# ARITHMETIC  OPERATORS
# print(8%3) #modulus
# print(45//11) #floor division(it gives value before point)
# print(2**4) #exponentiation
################################################
#COMPARISON OPERATORS
 
# print(5>3 )
# print(3!=5)
# print(3>=7)
#####################################
#LOGICAL OPERATORS

# print(3>7 and 4>3)
# print (3 == 3 or 3>5 )
# print (not(3>3 and 4>7))
############################################################
#ASSIGNMENT OPERATORS
# Simple assignment
# x = 10
# print("x =", x)   # Output: 10
##########################################
# Addition assignment
# x += 5
# print("x after += 5:", x)   # Output: 15
#################################################
# Subtraction assignment
# x -= 3
# print("x after -= 3:", x)   # Output: 12
###############################################
# Multiplication assignment
# x *= 2
# print("x after *= 2:", x)   # Output: 24
################################################
# Division assignment
# x /= 4
# print("x after /= 4:", x)   # Output: 6.0
#####################################################
# Modulus assignment
# x %= 5
# print("x after %= 5:", x)   # Output: 1.0
###############################################################
# Exponent assignment
# x **= 3
# print("x after **= 3:", x)  # Output: 1.0 (since 1^3 = 1)
################################################
#identity operator
#isnot
# a = 1234
# b = "1234"
# print(a is not b) #output : true
#############################################
#is
# a = 23
# b = 23
# print (a is b) # true

#BITWISE OPERATORS

# print(bin (15)) #bin use to calculate binary number 
##############################################
#AND 
# a = 32
# b = 34
# print(a & b) #AND operator
#####################################
#OR
# a = 11
# b = 34
# print (a | b) #output :- 43
###################################
#OR
# a = 10 
# b = 8
# print(a | b) # output :- 10
###########################
#EXOR
# a = 10 
# b = 8 
# print(a ^ b )  #output : - 2
#######################
#ZERO FILL LEFT SHIFT(>>)
# print (10>>1) #output : - 5

################
#ZERO FILL RIGHT SHIFT (<<)
# print (10 << 2) #output :- 40

###################
#membership operators
a = "Hello "
print("z" in a ) #False
print ("e" in a) # true 
print("x " is not a ) #true
