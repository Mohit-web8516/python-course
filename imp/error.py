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
