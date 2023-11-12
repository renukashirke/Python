# Exceptions are errors that crash our programs. They often happen because of bad
# input or programming errors. It’s our job to anticipate and handle these exceptions
# to prevent our programs from cashing.

try: 
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print('Not a valid number')
except ZeroDivisionError:
    print('Age cannot be 0')
