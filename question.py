#Generate the first n numbers in the Fibonacci sequence.
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# fibonacci(10)


#Prime Number Check
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# print(is_prime(29))  # True
#Palindrome String
# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("madam"))  # True
# print(is_palindrome("python")) # False


###############Factorial Using Recursion
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))  # 120



#############Armstrong Number

# def is_armstrong(num):
#     digits = str(num)
#     total = sum(int(d)**len(digits) for d in digits)
#     return total == num

# print(is_armstrong(153))  # True
# print(is_armstrong(123))  # False


####Reverse a Number

def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev

print(reverse_number(12345))  # 54321
