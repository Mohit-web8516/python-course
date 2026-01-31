###########LOOPS AND TYPES###############
############FOR LOOP
# for i in range (1,9):
#     print("hello world")
###########example
# Print numbers from 1 to 5
# for i in range(1, 6):
#     print(i)

#################example
# fruits = ["apple", "banana", "cherry","strawberry"]

# for fruit in fruits:
#     print("I like", fruit)

#####################while loop#############
#for odd number
# for i in range(1,6,2):
#     print(i)
#############
#for even number
# for i in range(0,6,2):
#     print(i)

############33for printing a table###############
# n = int(input("Enter a number: ")) 
# for i in range(1,11):
#     print(n, "X",i ,"=",n*i )

###############WHILE LOOP####################
# num = 1
# while num <= 10:
#     if num % 2 != 0:
#         print(num, "is odd")
#     num += 1
##########TABLE PRINTING USING WHILE LOOP
# n = 1
# a = 7
# while n<= 10:
#     print(a, "X" , n , "=", n*a)
#     n += 1
######################WHILE TRUE##########
# n = 1
# while True:
#     print(n)
#     n += 1  #it will never break
############################
# while True :
#     num1 = int(input("Enter a number here: "))
#     num2 = int(input("Enter another number here: "))
#     print(num1+num2)
#     repeat = input("Do you want to stop the program : ")
#     if repeat == "yes":
#         break
 
##############################NESTED LOOPS###################
# for i in range (1,4):
#     for j in range (1,11):
#         print(j, end = " ")
#     print()
#########PATTERN PRINTING USING NESTED LOOPS###########
# Print a triangle of stars
# for i in range(1, 6):          # outer loop (rows)
#     for j in range(i):         # inner loop (columns)
#         print("*", end=" ")
#     print()                    # move to next line
#############EXAMPLE OF PATTERN PRINTING
# for i in range (1,10):
#     for j in range(1,i+1):
#         print(j,end = " ")
#     print()


#############################FOR LOOP WITH CONDITIONAL STATEMENTS
# print("Odd and Even Numbers from 1 to 10:")

# for i in range(1, 11):   # loop from 1 to 10
#     if i % 2 == 0:
#         print(i, "is Even")
#     else:
#         print(i, "is Odd")

#############EXAMPLE--2#########
# marks = [95,92,85,75,60,30]

# for score in marks:
#     if score >= 90:
#         print(score,"GRADE A")
#     elif score >= 75 :
#         print(score,"GRADE B")
#     elif score >= 60:
#         print(score,"GRADE C") 
#     else:
#         print(score,"FAIL")
#####################EXAMPLE
# for i in range (1, 100):
#     if i % 8 == 0 and i % 12 == 0:
#         print(i)
################example
# n = 1
# while n <= 10:
#     if n == 3:
#         print("add this to favs")
#     else:
#         print(n)
#     n +=1

##################BREAK AND CONTINUE STATEMENT################
###BREAK STATEMENT

# for i in range(1, 11):
#     if i == 5:
#         break   # exit loop when i = 5
#     print(i)

#CONTINUE STATEMENT
# for i in range(1 , 11):
#     if i == 6:
#         continue 
#     print(i)



