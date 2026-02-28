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

# def reverse_number(num):
#     rev = 0
#     while num > 0:
#         digit = num % 10
#         rev = rev * 10 + digit
#         num //= 10
#     return rev

# print(reverse_number(12345))  # 54321


#####Sum Of Digit

def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

print(sum_of_digits(987))  # 24


###. Find Largest Element in a List

def find_max(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

print(find_max([10, 25, 3, 99, 45]))  # 99



##########Count Vowels in a String

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("rohini Developer"))  # 6

########Pattern Printing (Pyramid)

def pyramid(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "*" * (2*i-1))

pyramid(5)

