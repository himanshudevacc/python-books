# tuple is an immutable list
# tuple iteration is faster and consumes less memory than lists.
dimensionsInIJK = (50, 100, 40)  # it is a tuple

# dimensions[0] = 250
# TypeError: 'tuple' object does not support item assignment

# If you want to define a tuple with one element, you need to include a trailing comma:
myTuple = (3,)
print(myTuple, type(myTuple))

# looping
for dimension in dimensionsInIJK:
    print(dimension, end=" ")
print()

## Writing Over a Tuple -Although you can’t modify a tuple, you can assign a new value to a variable that represents a tuple.
coordinates = (3, 4, 5)
print("Initial Coordinates", coordinates)
coordinates = (1, 5, 3)
print("New Coordinates", coordinates)

# USE CASE: to store a set of values that should not be changed throughout the life of a program.
