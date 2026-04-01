# try:
#     x = 10 / 0   # This will raise ZeroDivisionError
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")


#################################################

# try:
#     num = int("abc")   # ValueError
# except ValueError:
#     print("Error: Invalid number format.")
# except ZeroDivisionError:
#     print("Error: Division by zero.")


###################################################

#. Using else and finally

try:
    num = int("25")
    print("Converted number:", num)
except ValueError:
    print("Error: Invalid input.")
else:
    print("No error occurred!")   # Runs only if no exception
finally:
    print("Execution finished!")  # Always runs


#####################################################

#Raising Exceptions Manually..


# def check_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative!")
#     return age

# try:
#     check_age(-5)
# except ValueError as e:
#     print("Error:", e)


##########################################################

# try:
#     num = int("25")
#     print("Converted number:", num)
# except ValueError:
#     print("Error: Invalid input.")
# else:
#     print("No error occurred!")   # Runs only if no exception
# finally:
#     print("Execution finished!")  # Always runs

######################################################

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

try:
    check_age(-5)
except ValueError as e:
    print("Error:", e)
