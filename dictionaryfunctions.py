############################################
# student = { "name ":"Harry Potter" ,"class":"5th","roll_no":"23"}

##################
#get
# x = student.get("roll_no")
# print(x)

#####################
#item
# a = student.items()
# print(a)
#########################
#keys
# b = student.keys()
# print(b)
#########################
#values
# c = student.values()
# print(c)
##########################
#copy
# f = student.copy()
# print(f)

#########################
#setdefault
# x = student.setdefault("course","python") #course will add to the dictionary
# print(x)
# print(student)

#############################
#pop
# g = student.pop("roll_no") #pop function delete the roll_no
# print(g)
# print(student) 
###########################
#popitem
# v = student.popitem()
# print(v)
# print(student)
############################
#update
# student.update({"age":34})
# print(student)

#########################
#clear()
# student.clear()
# print("dictionary after clear: ",student)

#######################################
######################################
#####################################
# #NESTED DICTIONARY
# students = {
#     101: {"name": "Harry Potter", "age": 21, "course": "Python"},
#     102: {"name": "Hermione Granger", "age": 22, "course": "Java"},
#     103: {"name": "Ron Weasley", "age": 20, "course": "C++"}
# }

# # Accessing nested values
# print(students)
# print(students[101]["name"])   # Harry Potter
# print(students[102]["name"])   # Hermione Granger
# print(students[103]["name"])   # Ron Weasley
# print(students[103])  
# print(students[103])  