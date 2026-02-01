#########################################
#question-1
#write a program to print fibonacci series up to 10 numbers.
# a = 0 
# b = 1
# n = int(input("Enter your number here : "))
# if n == 1:
#     print(1)
# else:
#     print (a)
#     print (b)
# for i in range (2,n):
#     c = a + b 
#     a = b
#     b = c
#     print (c)

######################################
#question-2
#write a program to check if a number is prime or not .
# num = int (input("enter your number here: "))

# if num <= 1:
#     print("it is not a prime number")
# else:
#     for i in range (2,num):
#         if num%i == 0:
#             print("number is not a prime number")
#             break
#     else:
#         print("it is prime number")

########################################
#write a program to find a palindrome of integers.

# num = int(input("enter a number here: "))
# temp = num
# rev = 0
# while num > 0:
#     dig = num%10
#     rev = rev*10+ dig 
#     num = num // 10

# if rev == temp:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

#######################METHOD 2

# num = int(input("Enter an integer: "))

# # Convert to string for easy reversal
# if str(num) == str(num)[::-1]:
#     print(num, "is a palindrome")
# else:
#     print(num, "is not a palindrome")

##############################################

#write a program to create an area calculator.
# Program to calculate area of different shapes

# while True:
#     print("\n--- Area Calculator ---")
#     print("1. Circle")
#     print("2. Rectangle")
#     print("3. Triangle")
#     print("4. Square")
#     print("5. Exit")

#     choice = input("Enter your choice (1-5): ")

#     if choice == '5':
#         print("Exiting Area Calculator... Goodbye!")
#         break

#     if choice == '1':
#         radius = float(input("Enter radius of circle: "))
#         area = 3.14159 * radius * radius
#         print("Area of Circle:", area)

#     elif choice == '2':
#         length = float(input("Enter length of rectangle: "))
#         width = float(input("Enter width of rectangle: "))
#         area = length * width
#         print("Area of Rectangle:", area)

#     elif choice == '3':
#         base = float(input("Enter base of triangle: "))
#         height = float(input("Enter height of triangle: "))
#         area = 0.5 * base * height
#         print("Area of Triangle:", area)

#     elif choice == '4':
#         side = float(input("Enter side of square: "))
#         area = side * side
#         print("Area of Square:", area)

#     else:
#         print("Invalid choice! Please select from 1 to 5.")

###########################################
###########################################
###########################################
#SOME OTHER PROBLEMS
# a = "OOTD,YOLO,ASAP,BRB,GTG,OTW"
#1...WRITE PROGRAM TO SEPARATE THE FOLLOWING STRING INTO COMMA(,) SEPARATED VALUES.

# b= a.split(",")
# print(b)
#2...WRITE A PROGRAM TO SORT STRINGS ALPHABETICALLY IN PYTHON

# a = input("enter anything here: ")
# b = sorted(a)
# print(b)
#WRITE A PROGRAM TO REMOVE A GIVEN CHARACTER FROM A STRING .
# a = "hello"
# b = a.replace("e","")
# print(b)
##############################################
# z = "F.R.I.E.N.D.S."
# #WRITE A PROGRAM TO REMOVE DOT(.) FROM THE FOLLOWING STRING.
# b = z.replace(".", "")
# print(b)
#WRITE A PROGRAM TO CHECK THE NUMBER OF OCCURRENCE OF A SUBSTRING IN A STRING
# a = "john is a cricketer and he is a good player "
# b = a.count("is")
# print("the number of time is  occuring is: ",b)
##############################################################
##############################################################
##############################################################
#QUESTION-1
#TAKE AN INPUT FROM A USER AS A STRING THEN,REVERSE IT.
# a = input("enter anything here : ")
# print(a[::-1])

# #WRITE A PROGRAM TO CHECK IF A STRING CONTAINS ONLY DIGITS.
# a = input("enter anything here : ")
# b = (a.isdigit())
# if b == True:
#     print("it contains only digits")
# else:
#     print("it does not contain only digits")

#WRITE A PROGRAM TO CHECK IF A STRING IS PALINDROME .
# a = input("enter anything here : ")
# rev = a[::-1]

# if a == rev:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

#WRITE A PROGRAM  TO FIND NUMBER OF VOWELS IN A STRING.

# a = input("Enter anything here: ")
# vowels = 0

# for i in a:
#     if i in "aeiouAEIOU":   # shorter way to check vowels
#         vowels += 1

# print("The number of vowels in the following string are:", vowels)

###########################################################
#WRITE A PROGRAM TO CHECK IF EVERY WORD IN A STRING BEGINS WITH A CAPITAL LETTER.
# a =input("enter anything here: ")
# print(a.istitle())