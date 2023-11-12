is_hot = True
is_cold = False

if is_hot:
    print("It's hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

print("Enjoy your day")

price = 1000000

has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

# Logical operators:

has_high_income = False
has_good_credit = True
has_criminal_record = False

if has_high_income or has_good_credit and not has_criminal_record:
    print("Eligible for loan")

# AND: both conditions should be true
# OR: at least one condition should be true
