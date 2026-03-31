# Iterable
# my_list = [10, 20, 30]

# # Convert to iterator
# iterator = iter(my_list)

# print(next(iterator))  # 10
# print(next(iterator))  # 20
# print(next(iterator))  # 30
# # next(iterator) would raise StopIteration


########################################################
#iterator using loop
# my_tuple = ("apple", "banana", "cherry")

# for item in my_tuple:   # internally uses iter() and next()
#     print(item)


##########################################################
'''Custom Iterator
You can build your own iterator by defining a class with __iter__() and __next__():'''

class CountDown:
    def __init__(self, start):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        current = self.num
        self.num -= 1
        return current

# Using custom iterator
for val in CountDown(5):
    print(val)
