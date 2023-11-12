# We use classes to define new types.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# When a function is part of a class, we refer to it as a method.
# Classes define templates or blueprints for creating objects. An object is an instance
# of a class. Every time we create a new instance, that instance follows the structure
# we define using the class.

point = Point(10, 20)
print(point.x)


# __init__ is a special method called constructor. It gets called at the time of
# creating new objects. We use it to initialize our objects.

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()
