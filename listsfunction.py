##############################################
##########LIST FUNCTION #########

a = ["Gandalf", "Dumbledore", "Merlin", "Harry","Ron","Hermione","Harry"]
#########to find length of a list
# #LENGTH
# print(len(a))

##to count an occurence of a particular elements
# print(a.count("Harry"))

#to add to the list
# #APPEND
# a.append("draco")
# print(a)

#To add to a specific location
#INSERT
# a.insert(3,"voldemort")
# print(a)

#to remove from a lost
#REMOVE
# a.remove("Harry")
# print(a)

#to remove from a certain location
#POP
# print(a.pop(1))
# print(a)

#TO CREATE A COPY OF A LIST
#COPY()
# b = []
# print(b)
# b = a.copy()
# print(b)
#TO ACCESS AN ELEMENT
#index
# print(a.index("Ron"))
#TO ENTEND THE LIST
#extend
# c = ["molly","sirius"]
# a.extend(c)
# print(a)
#TO REVERSE THE LIST
#reverse
# a.reverse()
# print(a)
#TO SORT THE LIST 
#sort
# a.sort()
# print(a)
##example of sort function
# d = [1,6,4,8,9,5,3,2]
# d.sort()
# print(d)
# a.sort()
#TO CLEAR ALL THE DATA FROM THE LIST
# a.clear()
# print(a) #or
# d.clear()
# print(d)

#################################################
#################################################
##########LIST COMPREHENSION#####################
# l1 = [20,30,40,50,60]
# l2 = []
# for i in l1:
#     l2.append(i)

# print(l1,"\n",l2)

# l3 = [i for i in l1 if i > 45]
# print(l3)
