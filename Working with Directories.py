from pathlib import Path

path = Path("ecommerce")
print(path.exists())

# path = Path("emails")
# print(path.mkdir())
# print(path.rmdir())

path = Path()
for file in path.glob('*.py'):
    print(file)
