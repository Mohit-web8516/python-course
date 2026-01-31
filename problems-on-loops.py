################QUESTION 1
####WRITE A PROGRAM TO FIND A SUM OF ALL THE EVEN NUMBERS UP TO 50

# sum  = 0
# for i in range(2,51,2):
#     sum += i 
# print("the sum of even numbers up to 50 is :" ,sum)
##second method ##################

# sum  = 0 
# for i in range (1,51):
#   if i% 2 == 0:
#     sum += i

# print("the sum of all the even number up to 50 is " , sum)


###############question 2
#write a program to writen first 20 numbers and their squared numbers

# for i in range(1,21):
#   print(i, "==", i**2)
 
#####################QUESTION 3#########################
#WRITE A PROGRAM TO FIND SUM OF FIRST 10 ODD NUMBERS USING WHILE LOOP

# n = 0 
# sum = 0
# while n <= 20:
#     if n %2 != 0:
#         sum += n
#     n += 1
# print("the sum of first 10 0dd numbewrs is" , sum)

######################problem 4##################

#################WRITE A PROGRAM TO CHECK IF A NUMBER IS DIVISIBLE BY 8 AND 12 ,UP TO 100 NUMBERS.
# num = int(input("Enter the number: "))

# if num % 8 == 0 and num % 12 == 0:
#     print(num, "is divisible by 8 and 12")
# else:
#     print(num, "is NOT divisible by 8 and 12")

###############PROBLEM 5####################
#WRITE A PROGRAM to CREATE A BILING SYSTEM AT SUPERMARKET.

# print("***** SUPERMARKET BILLING SYSTEM *****")

# while True:   # outer loop for customers
#     name = input("Enter customer's name: ")
#     total = 0

#     while True:   # inner loop for items
#         print("Enter the amount and quantity")
#         amount = float(input("Enter amount: "))
#         quantity = int(input("Enter quantity: "))
#         total += amount * quantity

#         repeat = input("Do you want to add more items? (yes/no): ")
#         if repeat == "no":
#             break

#     # Print bill for this customer
#     print("-" * 40)
#     print("Customer Name:", name)
#     print("Amount to be paid:", total)
#     print("-" * 40)
#     print("****** Happy Shopping ***********")

#     # Ask if we want to move to next customer
#     repeat1 = input("Do you want to go to next customer? (yes/no): ")
#     if repeat1 == "no":
#         break

##################### STRING QUESTION ####################
# a = "Hey how are you dude? this side john!!"

########to calculate length of string 
# print(len(a))
#  #or 
# b = (len(a))
# print("the length of the given string is ", b)

####################to check how many time alphabet o is occurring

# print(a.count("o"))

#####################program to convert the whole string into lower and upper case
# x = a.lower()
# print(x)
# y = a.upper()
# print(y)
###############capitalize whole string 
# w = a.title()
# print(w)
################### write program to find index number of "you dude"
# print(a.find("you dude"))