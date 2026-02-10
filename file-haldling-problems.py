with open ("practice.txt", "w") as f:
    f.write("Hi everyone\n we are learning file i/o \n")
    f.write("using java.\ni like programming in java.")

###write a function that replaces all the occurrences of "java " with "python" in above file.
# with open ("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("java","python")
# print(new_data)

# with open ("practice.txt","w") as f:
#   f.write(new_data)


######################################
# word = "learning"
# with open("practice.txt","r") as f:
#     data = f.read()
#     if (data.find(word) != -1 ):
#         print("found")
#     else:
#         print("not found")


####################################################
#write a function to find out thwe exact line at which word learning occur
# def check_for_word():
#     word = " xlearning"
#     with open ("practice.txt", "r") as f:
#         data = f.read()
#         if(word in data ):
#             print("found")
#         else:
#             print("not found")
#######################################################
# def check_for_line():
#     word = "python"
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         for line in f:  # iterate directly over lines
#             if word in line:
#                 print(line_no)
#                 return line_no
#             line_no += 1
#     return -1
# print(check_for_line())

###########################################################
#
count = 0
with open ("demo.txt", "r") as f:
    data = f.read()
    print (data)

nums = data.split(",")  
for val in nums:
    if (int(val) % 2== 0):
        count += 1

print(count)