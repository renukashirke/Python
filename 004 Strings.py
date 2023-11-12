# We can define strings using single (' ') or double (" ") quotes.
# To define a multi-line string, we surround our string with tripe quotes (''').
# We can get individual characters in a string using square brackets [].

course = 'Python for Beginners'
print(course)
print(course[0])  # returns the first character
print(course[1])  # returns the second character
print(course[-1])  # returns the first character from the end
print(course[-2])  # returns the second character from the end

# We can slice a string using a similar notation:

print(course[1:5])

# The above expression returns all the characters starting from the index position of 1
# to 5 (but excluding 5). The result will be ytho
# If we leave out the start index, 0 will be assumed.
# If we leave out the end index, the length of the string will be assumed.
# We can use formatted strings to dynamically insert values into our strings:

name = 'Renuka'
message = f'Hi, my name is {name}.'
print(message)
print(message.upper())  # to convert to uppercase
print(message.lower())  # to convert to lowercase
print(message.title())  # to capitalize the first letter of every word
print(message.find('i'))  # returns the index of the first occurrence of p (or -1 if not found)
print(message.replace('Renuka', 'Renu'))

# To check if a string contains a character (or a sequence of characters), we use the in operator:

contains = 'Python' in course
print(contains)
