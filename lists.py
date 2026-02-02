###################################################
#LISTS
# fruits = ["apple","mango","strawberry","orange"]
# print(fruits)
# print(type(fruits))

################EXAMPLE
# fruits = ["apple","mango","strawberry","orange",12,12.4,56.00]
# print(fruits)
# print(type(fruits))

#####################SLICING LISTS########################
# cart = ["milk", "bread", "eggs", "butter", "jam", "cheese"]

# Get first 3 items
# print(cart[:3])   # Output: ['milk', 'bread', 'eggs']

# Get last 2 items
# print(cart[-2:])  # Output: ['jam', 'cheese']

# Get alternate items
# print(cart[::2])  # Output: ['milk', 'eggs', 'jam']

############################################################
# a = ["ironman","thor","captain america","hulk"]
# print(a[-2])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[1:3])
# print(a[::2])
# print(a[-3:-1])
# print(a[::-1])
# print(a[-1:-4:-1])

####################################################
###################################################
#LIST ITERATION
#ITERATION USING FOR LOOP
# wizards = ["Gandalf", "Dumbledore", "Merlin", "Harry"]

# for wizard in wizards:
#     print(wizard)
#######################################################################
#ITERATION USING FOR LOOP WITH RANGE AND LENGTH FUNCTION:

# wizards = ["Gandalf", "Dumbledore", "Merlin", "Harry"]

# for wizard in range(len(wizards)):
#     print(wizards[wizard])

###############################################
#ITERATION USING WHILE LOOP
# wizards = ["Gandalf", "Dumbledore", "Merlin", "Harry"]

# i = 0
# while i < len(wizards):   # loop until index reaches list length
#     print(wizards[i])
#     i += 1   # move to the next index

##################################################
#USING SHORT -HAND FOR LOOP
# wizards = ["Gandalf", "Dumbledore", "Merlin", "Harry"]
# [print(wizard) for wizard in wizards]

