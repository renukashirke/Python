# We can receive input from the user by calling the input() function.

name = input('What is your name? ')
favorite_color = input('What is your favorite color? ')
print(name + ' likes ' + favorite_color)

birth_year = input('Birth year: ')
# print(type(birth_year))
age = 2023 - int(birth_year)
# print(type(age))
print(age)

# The input() function always returns data as a string. So, we’re converting the
# result into an integer by calling the built-in int() function.

weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
