def prime_num(num):
    if num == 1:
        print("it is not a prime number")
    if num == 2:
        print("it is a prime number")
    if num>2:
     for i in range (2,num):
        if num % i == 0:
            print("it is not a prime number")
            break
    else:
        print("it is a prime number")

prime_num(13)
