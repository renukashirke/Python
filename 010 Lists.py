numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # returns the first item
print(numbers[1])  # returns the second item
print(numbers[-1])  # returns the first item from the end
print(numbers[-2])  # returns the second item from the end

numbers.append(6)  # adds 6 to the end
print(numbers)

numbers.insert(0, 6)  # adds 6 at index position of 0
print(numbers)

numbers.remove(6)  # removes 6
print(numbers)

numbers.pop()  # removes the last item
print(numbers)

numbers.clear()  # removes all the items
print(numbers)

numbers = [6, 4, 1, 8, 5]

print(numbers.index(8))  # returns the index of first occurrence of 8

numbers.sort()  # sorts the list
print(numbers)

numbers.reverse()  # reverses the list
print(numbers)

print(numbers.copy())  # returns a copy of the list

# find the largest number in a list

numbers = [3, 6, 2, 8, 4, 10]
maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number
print(maximum)

# 2D Lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)
print(matrix[0][1])

matrix[0][1] = 20
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

# remove duplicates in a list

numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
