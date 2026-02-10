"""
"r"	Read (default). File must exist.
"w"	Write. Creates new file or overwrites existing.
"a"	Append. Adds data at the end of file.
"r+"	Read and write. File must exist.
"b"	Binary mode (e.g., "rb", "wb").

"""
#++++++++++++++++++++TO OPEN A FILE +++++++
f = open("demo.txt",'r')
# data = f.read()
# data = f.read(5) ##to specify numbers to read
# print(data)
# print(type(data))
# f.close()


#######################################
#TO READ A LINE 
# line1 = f.readline()
# print(line1)

# f.close()
###############################


# line2 = f.readline()
# print(line2)

# f.close()


###############################
###############################
###############################
###############################
###############################
#TO WRITE DATA IN A FILE
# Open file in write mode
file = open("demo.txt", "w")

# Write text into the file
file.write("Hello, world!\n")
file.write("This is a new line.\n")
file.write("This is a new red line.\n")

# Always close the file
file.close()
##############################
##############################
##############################
##############################
##############################
#TO APPEND  DATA IN A FILE
# Open file in append mode
# file = open("demo.txt", "a")

# # Add new lines at the end
# file.write("This is an appended line.\n")
# file.write("Another line added.\n")

# file.close()



#########################################
##################################
# with open ("demo.txt","r") as f:
#     data = f.read()
#     print(data)

# with open("demo.txt","w") as f:
#     f.write("new data ")






########################################
########################################
########################################
########################################
########################################
########################################
#DELETING A FILE
# import os

# # Specify the file name
# file_name = "example.txt"

# # Delete the file
# os.remove(file_name)
# print("File deleted successfully!")
