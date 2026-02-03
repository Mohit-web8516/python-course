#write a program to find max and min in a set.
# numbers = {10, 25, 3, 45, 7}
# maximum = max(numbers)
# minimum = min(numbers)
# print("Maximum value in the set :", maximum)
# print("Minimum value in the set :", minimum)
##########################################################
#write a program to find common elements in three lists using sets.
# a = [1,2,3,5,6,7,8]
# b = [5,6,2,3,7,8]
# c = [1,29,0,6,7,8]
# print("the common elements  in the given three lists are :",set(a) & set(b) & set(c))
#############################################################
#write a program to find the difference between two sets.
# a = {1,2,3,5,6,7,8}
# b ={ 5,6,2,3,7,8}
# print(a.difference(b))
# print(b.difference(a))
#################################################################
#write a python program to remove an item from a set if it is present in the set.
##########method 1
# a ={ 5,6,2,3,7,8}
# a.discard(9) # GIVE SAME SET 
# a.discard(7) # give {2, 3, 5, 6, 8}
# print(a)
################################
######IMPROVED METHOD 
# fruits = {"apple", "banana", "cherry"}

# item = "banana"
# if item in fruits:
#     fruits.remove(item)

# print("Updated set:", fruits)
###########################################################
#write a python program program to check if a set is a subset of another set.
# a = {1,3,4,5,6,2}
# b = { 4,5,2}
# print(b.issubset(a)) #true
# print(a.issubset(b)) #false
