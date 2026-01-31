####################
#IF STATEMENT
# marks = 10 
# if marks >= 2:
#     print ("you will get a mobile phone ")
# print ("thank you!")
###############
# #IF-ELSE STATEMENT
# pens = 20
# if pens >= 30:
#     print("You have extra pen !") 
# else :
#     print("You don't have enough pens!")
# print("Thank you!")
######################
#IF-ELIF-ELSE STATEMENT
# color = "blue"

# if color == "blue":
#     print("YOU have a correct one!")
# elif color == "grey": 
#     print("You don't have the same color!")
# else:
#     print("Try again!")

# print("Thank you!")

###########EXAMPLE--2##################
# A program that responds based on user's favorite color

# Ask the user for input
# color = input("Enter your favorite color: ").lower()   # .lower() makes the user input in lower case 

# if color == "blue":
#     print("Blue is calming, like the sky and ocean.")
# elif color == "red":
#     print("Red is bold and full of energy!")
# elif color == "green":
#     print("Green reminds me of nature and peace.")
# elif color == "yellow":
#     print("Yellow is bright and cheerful, like sunshine.")
# elif color == "black":
#     print("Black is elegant and powerful.")
# elif color == "white":
#     print("White feels pure and simple.")
# else:
#     print("That's an interesting choice! I don't have info about that color yet.")

# print("Thanks for sharing your favorite color!")
 
##############EXAMPLE---3#######################

# print("Welcome to the Travel Recommendation Program!")
# print("Tell me your mood, and I'll suggest a destination.")
# print("Options: happy / tired / adventurous / romantic / curious")

# mood = input("Enter your mood: ").lower()

# if mood == "happy":
#     print("You should go to Disneyland 🎢 — happiness everywhere!")
# elif mood == "tired":
#     print("A calm beach vacation 🏖️ will help you relax.")
# elif mood == "adventurous":
#     print("Head to the Himalayas 🏔️ for trekking and thrill!")
# elif mood == "romantic":
#     print("Paris ❤️ is the city of love, perfect for romance.")
# elif mood == "curious":
#     print("Visit the Egyptian Pyramids 🏜️ to explore history.")
# else:
#     print("I don't have a suggestion for that mood yet, but keep exploring!")

# print("Thanks for using the Travel Recommendation Program!")

#############################################
#NESTED-IF STATEMEMT
# marks = 90
# if marks >= 80:
#     print("You will get a new phone")
#     if marks >= 85:
#         print("You will go to a trip!")
# else:
#     print("No phone for a month!")

##################example-2#######################

# print("Welcome to the Movie Ticket System!")

# age = int(input("Enter your age: "))
# day = input("Enter the day (weekday/weekend): ").lower()

# if age >= 18:
#     print("You are eligible to watch adult movies.")
    
    # Nested if inside the age condition
#     if day == "weekday":
#         print("Ticket price is 200 INR.")
#     elif day == "weekend":
#         print("Ticket price is 300 INR.")
#     else:
#         print("Invalid day entered.")
# else:
#     print("You can only watch children's movies.")
    
    # Nested if inside the else condition
#     if day == "weekday":
#         print("Ticket price is 150 INR.")
#     elif day == "weekend":
#         print("Ticket price is 200 INR.")
#     else:
#         print("Invalid day entered.")

# print("Enjoy your movie!")

#######################################3
#SHORT HAND IF STATEMENT

# marks = 87
# print("you will go to a trip ") if marks >= 90 else print ("no phone for a month ")

#############EXAMPLE--2##############
# Example: Checking if a number is positive or negative
# number = -5
# result = "Positive" if number > 0 else "Negative"
# print(result)

###################EXAMPLE ---3##################
# age = 18
# print("Adult") if age >= 18 else print("Minor")

##################PROBLEM SOLVING
#check a number is positive or negative
# num = int(input("Enter a number here : "))
# if num > 0 :
#     print("It is a positive number! ")
# else:
#     print("Its is a negative number! ")

##################problem---2##############
#check a number is odd or even
# num = int(input("Enter a number here : "))
# if num % 2 ==0:
#     print ("Number is Even! ")
# else:
#     print ("Number is odd! ")

###################problem--3##############
#write a program  to create  area calculator.
# print("*****AREA CALCULATOR*****")
# print(""" press 1 to get the area of square 
#       press 2 to get the area of rectangle
#       press 3 to get the area of circle 
#       press 4 to get the area of triangle """)

# choice = int(input("Enter a number between 1-4 : "))
# if choice == 1 :
#     side = float(input("Enter the length of one side : "))
#     area = side**2
#     print ("the area of square is " ,area)

# elif choice == 2:
#     length = float(input("Enter length of the rectangle: "))
#     width= float(input("Enter width of the rectangle: "))
#     area = length*width
#     print("the area of rectangle is ", area)

# elif choice == 3:
#     radius = float(input("Enter the radius of the circle: "))
#     area = (22/7) * radius ** 2
#     print("The area of the circle is:", area)

# elif choice == 4:
#     base = float(input("Enter the base of the triangle: "))
#     height = float(input("Enter the height of the triangle: "))
#     area = 0.5 * base * height
#     print("The area of the triangle is:", area)

# else:
#     print("Invalid choice! Please enter a number between 1-4.")

# print("***** Thank you for using the Area Calculator *****")

#########################PROBLEM --4########################
#WRITE A PROGRAM CHECK WHEATHER THE PASSED LETTER IS A VVOWEL OR NOT

# print("** VOWEL CHECKER **")

# ch = input("Enter a single alphabet: ").lower()   # convert to lowercase for easy comparison

# # # Check if input is a vowel
# if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch=="A" or ch == "E"or ch== "I" or ch == "O" or ch == "U":
#     print("The alphabet", ch, "is a VOWEL.")
# else:
#     print("The alphabet", ch, "is NOT a vowel.")

# print("DONE!!!!!!!!!!!!!!")

############second method########
# letter = input("Enter a letter here: ")
# if letter in "aeiou" or letter in "AEIOU":
#     print("it is a vowel!")
# else :
#     print("Its not a vowel!")
####################PROBLEM--5##################
#WRITE A PROGRAM TO CHECK IF A NUMBWER IS A SINGLE DIGIT NUMBER ,2-DIGIT NUMBER AND SO ON ....,UP TO 5 DIGITS.

# num = int (input("Enter your number here up to 5 digits :  "))

# # Check the number of digits
# if num >= 0 and num <= 9:
#     print("It is a SINGLE digit number.")
# elif num >= 10 and num <= 99:
#     print("It is a TWO digit number.")
# elif num >= 100 and num <= 999:
#     print("It is a THREE digit number.")
# elif num >= 1000 and num <= 9999:
#     print("It is a FOUR digit number.")
# elif num >= 10000 and num <= 99999:
#     print("It is a FIVE digit number.")
# else:
#     print("Number is more than 5 digits or negative.")

# print("Done!!!!!!!!!!!")
























































# print("Welcome to the Adventure Game!")
# print("You are standing at a crossroad. Where do you want to go?")
# print("Options: forest / cave / village")

# choice = input("Enter your choice: ").lower()

# if choice == "forest":
#     print("You walk into the forest. It's peaceful, but you hear rustling in the bushes...")
#     print("Do you want to investigate or run?")
#     action = input("Enter investigate/run: ").lower()
#     if action == "investigate":
#         print("A friendly deer appears 🦌. You made a new friend!")
#     elif action == "run":
#         print("You run back safely to the crossroad.")
#     else:
#         print("You hesitate too long and the moment passes.")

# elif choice == "cave":
#     print("You enter the dark cave. It's cold and damp.")
#     print("Suddenly, you see glowing eyes 👀. Do you fight or escape?")
#     action = input("Enter fight/escape: ").lower()
#     if action == "fight":
#         print("You bravely fight the creature and find hidden treasure 💎!")
#     elif action == "escape":
#         print("You escape safely, but miss out on the treasure.")
#     else:
#         print("You freeze in fear... the creature disappears mysteriously.")

# elif choice == "village":
#     print("You arrive at a small village. People welcome you warmly 🏡.")
#     print("Do you want to stay or continue your journey?")
#     action = input("Enter stay/continue: ").lower()
#     if action == "stay":
#         print("You live happily among the villagers. Game over 😊.")
#     elif action == "continue":
#         print("You leave the village and return to the crossroad.")
#     else:
#         print("You wander around confused until night falls.")

# else:
#     print("That's not a valid choice. Try again!")

# print("Thanks for playing the Adventure Game!")



