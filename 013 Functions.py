# We use functions to break up our code into small chunks. These chunks are easier
# to read, understand and maintain. If there are bugs, it’s easier to find bugs in a
# small chunk than the entire program. We can also re-use these chunks.

def greet_user1():
    print('Hi there!')
    print('Welcome aboard')


print("Start")
greet_user1()
print("Finish")


def greet_user2(name):
    print(f"Hi {name}")


greet_user2("Renuka")


# Parameters are placeholders for the data we can pass to functions. Arguments
# are the actual values we pass.
# We have two types of arguments:
# • Positional arguments: their position (order) matters
# • Keyword arguments: position doesn't matter - we prefix them with the parameter
# name.

# Two positional arguments


def greet_user3(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")


greet_user3("John", "Smith")


# Keyword arguments


def calculate_total(order, tax, shipping):
    return order + tax + shipping


print(calculate_total(order=50, shipping=5, tax=0.1))

# Our functions can return values. If we don’t use the return statement, by default
# None is returned. None is an object that represents the absence of a value.


def square(number):
    return number * number


result = square(3)
print(result)
