#######################################
#add()
# fruits = {"apple", "banana"}
# fruits.add("cherry")
# print(fruits)   # {'apple', 'banana', 'cherry'}

############################################
#update()
# fruits = {"apple", "banana"}
# fruits.update(["cherry", "mango"])
# print(fruits)   # {'apple', 'banana', 'cherry', 'mango'}
################################
#remove()
# fruits = {"apple", "banana", "cherry"}
# fruits.remove("banana")
# print(fruits)   # {'apple', 'cherry'}

######################################
#discard
# fruits = {"apple", "banana"}
# fruits.discard("grape")   # no error if grape not found
# print(fruits)   # {'apple', 'banana'}
###################################
#pop()
# fruits = {"apple", "banana", "cherry"}
# removed = fruits.pop()
# print("Removed:", removed)
# print("Remaining:", fruits)

####################################
#copy()
# fruits = {"apple", "banana"}
# new_fruits = fruits.copy()
# print(new_fruits)   # {'apple', 'banana'}

###################################
#isdisjoint
# a = {1, 2, 3}
# b = {4, 5, 6}
# c = {3, 4, 5}

# print(a.isdisjoint(b))  # True (no common elements)
# print(a.isdisjoint(c))  # False (common element: 3)
# print(a.isdisjoint(a)) #false( all common element)
##################################
# issubset
# x = {1, 2}
# y = {1, 2, 3, 4}

# print(x.issubset(y))   # True (all elements of x are in y)
# print(y.issubset(x))   # False 
#####################################

# issuperset
# x = {1, 2}
# y = {1, 2, 3, 4}

# print(y.issuperset(x))   # True (y contains all elements of x)
# print(x.issuperset(y))   # False
###########################################
# update
# a = {"apple", "banana"}
# b ={"cherry", "mango","banana"}
# a.update(b)
# print(a)

###########################################
# clear
# a = {"apple", "banana"} 
# print(a.clear())
# print(a)
#########################################
#union 

# a = {1,3,5,6,7,8}
# b = {3,7,8,5,3,9}
# print(a.union(b))
#####################################
#difference
# print(a.difference(b))
# print(b.difference(a))
# print(a.difference(a)) #empty set
####################################
# difference update 
# a = {1, 2, 3, 4}
# b = {3, 4, 5}
# a.difference_update(b)
# print(a)   # {1, 2}

###################################
# intersection
# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a.intersection(b))   # {2, 3}
# print(b.intersection(a)) #{2, 3}
#########################################
# intersection update
# a = {1, 2, 3, 4}
# b = {2, 3}
# a.intersection_update(b)
# b.intersection_update(a)
# print(a)   # {2, 3}
# print(b)   #{2, 3}
####################################
# symmetric diffrence :- Returns elements that are in either set but not both.
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.symmetric_difference(b))   # {1, 2, 4, 5}
#####################################

# symmetric difference update
# a = {1, 2, 3}
# b = {3, 4, 5}
# a.symmetric_difference_update(b)
# print(a)   # {1, 2, 4, 5}
