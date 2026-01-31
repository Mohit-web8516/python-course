#############string creation#############
# a = "hello world"
# print(type(a))
# print(a)

#################operations#######
#LENGTH
# a = "hello john"
# print(len(a))

##################################
#COUNT
# a = "hello john"
# print(a.count("l"))

#################################
#UPPER
# a = "hello john"
# print(a.upper())

################################
#LOWER
# a = "hello john"
# print(a.index("j"))

################################
#CAPITALIZE
# a = "hello john"
# print(a.capitalize()) #capitalize only first letter

################################
#CASEFOLD
# text = "Python"
# print(text.casefold())   #(BASICALLY A STRONG .lower())

####ONE MORE EXAMPLE OF CASEFOLD###
# word1 = "straße"        # German word for street
# word2 = "strasse"

# print(word1.lower() == word2)      # False
# print(word1.casefold() == word2)   # True

####################one more example of casefold######
# word1 = "CAFÉ"
# word2 = "cafe"

# print(word1.lower() == word2)      # False
# print(word1.casefold() == word2)   # False

############example of casefold###############

# a = "Hello ,How are you?"
# print(a.casefold()) #convert capital letter into small letter

###############################
#FIND
# text = "Python"
# print(text.find("t"))   #tells about index of "t"

#############################
#FORMAT
# name = "Alex"
# a = "My name is {}"
# print(a.format(name))

########################EXAMPLE OF FORMAT#########
# name = "john"
# age = 25

# print("My name is {} and I am {} years old.".format(name, age))

#########################################
#CENTER
# name = "John"
# age = 20

# print(name.center(20,"*"))      #*******John********

        #######################################
        #######################################
        #######################################
            #STRING OPERATIONS PART -2##
######################
#ISALNUM () 
"""isalnum() is a string method that checks if all characters in a string are alphanumeric (letters A–Z or digits 0–9).

If the string contains only letters and/or digits, it returns True.

If there are spaces, symbols, or special characters, it returns False."""
#########EXAMPLES#################
# print("Python3".isalnum())     # True (letters + digits)
# print("12345".isalnum())       # True (only digits)
# print("HelloWorld".isalnum())  # True (only letters)
# print("Hello World".isalnum()) # False (space not allowed)
# print("Hello!".isalnum())      # False (special character !)
# print("".isalnum())            # False (empty string)

################################
#ISALPHA()
"""Checks if all characters in the string are alphabetic letters (A–Z, a–z, or Unicode letters).

Returns True if the string contains only letters.

Returns False if the string contains digits, spaces, or special characters."""

##########EXAMPLE
# print("Python".isalpha())     # True (only letters)
# print("HelloWorld".isalpha()) # True (only letters)
# print("Hello123".isalpha())   # False (contains digits)
# print("Hello World".isalpha())# False (contains space)
# print("".isalpha())           # False (empty string)

##############################
####ISDECIMAL()
"""Checks if all characters in the string are decimal digits (0–9).

Returns True for standard digits only.

Returns False if the string contains letters, spaces, or non-decimal numeric characters (like fractions or Roman numerals)."""

###########EXAMPLE
# print("123".isdecimal())      # True (only digits)
# print("007".isdecimal())      # True (leading zeros are fine)
# print("12.5".isdecimal())     # False (decimal point not allowed)
# print("Ⅷ".isdecimal())        # False (Roman numeral 8 is numeric but not decimal)
# print("".isdecimal())         # False (empty string)

###############################
#ISDIGIT()
"""Returns True if all characters in the string are digits (0–9).

Works only for standard decimal digits.

Does not recognize fractions, Roman numerals, or other numeric symbols"""

#############EXAMPLE
# print("123".isdigit())     # True (only digits)
# print("007".isdigit())     # True (leading zeros are fine)
# print("12.5".isdigit())    # False (decimal point not allowed)
# print("Ⅷ".isdigit())       # False (Roman numeral 8 is not a digit)
# print("²".isdigit())       # True (superscript 2 counts as a digit)

###############################
#ISNUMERIC()
"""Returns True if all characters are numeric, including digits, fractions, superscripts, Roman numerals, etc.

More general than isdigit()"""

# print("123".isnumeric())   # True (digits)
# print("Ⅷ".isnumeric())     # True (Roman numeral 8)
# print("²".isnumeric())     # True (superscript 2)
# print("½".isnumeric())     # True (fraction one-half)
# print("12.5".isnumeric())  # False (decimal point not allowed)

###############example
# a = "1234"
# print(a,a.isnumeric())

#################################
#ISLOWER() (ALL CHARACTER OF A STRING  SHOULD  BE IN LOWERCASE)

#########EXAMPLE
# print("hello".islower())      # True (all lowercase)
# print("hello123".islower())   # True (digits ignored)
# print("Hello".islower())      # False (H is uppercase)
# print("HELLO".islower())      # False (all uppercase)
# print("".islower())           # False (empty string)

####################################
#ISUPPER() (ALL CHARACTER OF A STRING SHOULD BE IN UPPERCASE)

##########EXAMPLE
# print("HELLO".isupper())      # True (all uppercase)
# print("HELLO123".isupper())   # True (digits ignored)
# print("Hello".isupper())      # False (e is lowercase)
# print("hello".isupper())      # False (all lowercase)
# print("".isupper())           # False (empty string)


###################################
#ISSPACE()
"""Checks if all characters in the string are whitespace.

Whitespace includes: spaces (" "), tabs ("\t"), newlines ("\n").

Returns True if the string contains only whitespace characters.

Returns False if there are any non-whitespace characters or if the string is empty"""

##################EXAMPLE
# print("   ".isspace())     # True (only spaces)
# print("\t".isspace())      # True (tab is whitespace)
# print("\n".isspace())      # True (newline is whitespace)
# print(" hello ".isspace()) # False (letters included)
# print("".isspace())        # False (empty string)


####################################
#ISTITLE()
##ITS GIVE TRUE WHEN FIRST LETTER OF EACH WORD IS UPPERCASE AND REMAINING LETTERS IN LOWERCASE ,OTHERWISE IT RETURN FALSE .

#######################example
# a = "John Is a Good Boy And Also Intelligent " 
# print(a,a.istitle()) #false because "a" is in lowercase

##################EXAMPLE
# print("Hello World".istitle())   # True (each word starts with uppercase)
# print("Python Programming".istitle()) # True
# print("Hello world".istitle())   # False (second word not capitalized)
# print("HELLO World".istitle())   # False (first word all uppercase)
# print("hello world".istitle())   # False (all lowercase)

        #######################################
        #######################################
        #######################################
        ############STRING FUNCTION PART --3##
#################################
#ENDWIDTH()
#RETURNS TRUE IF THE STRING ENDS WITH THE SPECIFIED VALUE 

# a = "Harry Potter"
# print(a.endswith("p")) #false
# print(a.endswith("r")) #true

##################################
##########STARTSWITH()
#RETURNS TRUE IF THE STRING STARTS WITH THE SPECIFIED VALUE.

# a = "Harry Potter"
# print(a.startswith("p")) #false("case-sensitive")
# print(a.startswith("H")) #true 

################################
#SWAPCASE()
#SWAPS CASES ,LOWER CASE BECOMES UPPER CASE AND VICE VERSA 

# a = "Harry Potter"
# print(a.swapcase()) 

##########################################
#strip()
#returns a trimmed version of the string 
# a = "     Harry Potter      " 
# print(a.strip()) 

##################example
# a = "    ****** Harry Potter ........     " #
# print(a.strip(".,*, ")) # trimmed all the "*" and "." and whitespaces

#####################################
#split()
#splits the strings at the specified separator ,and returns a list 

# a = "hey ,my name is john and im 25 year old!" 
# print(a.split()) 


###########################################
#ljust()
#returns a left justified version of the string 
# a = "Harry Potter"
# x = a.ljust(20,"*")
# print(x,"is my favorite movie") 

##########################################
#rjust()
#returns a right justified version of the string

# a = "Harry Potter"
# x = a.rjust(20,"*")
# print(x,"is my favorite movie")

############################################
#REPLACE()
#RETURNS A STRING WHERE A SPECIFIED VALUE IS REPLACE WITH A
# a = " my name is john"
# print (a)
# print (a.replace("john","lisa"))

##############################################
#rindex()
#searches the string foa a specified value and the returns the last position of where it was found 

# a = "Harry potter and the Prisoner of Azkaban"
# print(a.rindex("Azkaban"))

###############################################
#rfind()
#searches the string for a specified value and returns the last position of where it was found

# a = "Harry potter and the Prisoner of Azkaban"
# print(a.rfind("potter"))
# print(a.rfind("he",15, 23))
