# We use dictionaries to store key/value pairs.

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])

# We can use strings or numbers to define keys. They should be unique. We can use
# any types for the values.

print(customer.get("birthdate"))

print(customer.get("birthdate", "Jan 1 1980"))

customer["name"] = "Jack Smith"

customer["birthdate"] = "Jan 1 1980"

print(customer)

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)
