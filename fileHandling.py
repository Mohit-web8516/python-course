#Reading file 

# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()
############################################

# file = open("example.txt", "r")
# for line in file:
#     print(line.strip())
# file.close()


############################################
#Writing a file

# file = open("example.txt", "w")
# file.write("Hello, JOHN!\n")
# file.write("This is a new line.")
# file.close()


###############################################
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

########################################
# Writing text to a file
# with open("example.txt", "w") as f:
#     f.write("Hello john!\n")
#     f.write("This is a file handling example.")




########################################
# # Reading the entire file
# with open("example.txt", "r") as f:
#     content = f.read()
#     print("File content:\n", content)
############################################

# Reading line by line
# with open("example.txt", "r") as f:
#     for line in f:
#         print("Line:", line.strip())
#####################################################

# Adding new content without overwriting
# with open("example.txt", "a") as f:
#     f.write("\nThis line is appended.")


###############################################
try:
    with open("nonexistent.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("Error: File does not exist!")

