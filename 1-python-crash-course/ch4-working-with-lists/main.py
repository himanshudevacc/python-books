## Looping through a list
magicians = ["alice", "david", "carolina", "george", "calm"]
position = 1
for magician in magicians:
    print(f"coming in position {position} we have {magician.title()}")
    position += 1
print("values variables: position & magician respectively", position)
# print(magician) throws error because "magician" var is not defined after loop execution
print("Thank you, everyone. That was a great magic show!\n")

## exercise
pizzas = ["paneer", "barbeque", "farmhouse"]
for pizza in pizzas:
    print(f"I love eating {pizza} pizza.")
print("I really love pizza")


## Numerical lists
# using range() function - it is an inbuilt python function
print(type(range(1, 4)))  # <class 'range'>
# use cases : 1st- for loop , 2nd- if i in range(a,b) => returns boolean
print(2 in range(1, 4))  # true
print(2.4 in range(1, 4))  # false, as range only deals with integers

for no in range(1, 10):
    print(no, end=",")
print("these are all one digit whole nos")

# 3rd usecase: generate list with list(range(a,b))
evenNos = list(range(2, 11, 2))
print(evenNos)  # [2, 4, 6, 8, 10]

squareNos = []
for no in range(1, 11):
    squareNos.append(no**2)
print(squareNos)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

## min,max,sum function
print(min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 1
print(max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 10
print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 55


## Instead of creating an empty list and using the append method use list comprehension
oddNosSquares = [oddNo * oddNo for oddNo in range(1, 10, 2)]
print(oddNosSquares)  # [1, 9, 25, 49, 81]


## Slicing - list[start:stop:step]
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(array[3:8])  # [4,5,6,7,8]

# to access last 'n' elements use list[:-n]
print(array[-3:])  # [5, 6, 7, 8, 9]

print(array[::-1])  # reverse the list [9, 8, 7, 6, 5, 4, 3, 2, 1]


## looping through a slice
players = ["charles", "martina", "michael", "florence", "eli"]

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())


## Copying a List - assigning a variable a sliced copy(eg: lst1 = lst2[:]) is a good practice of copying because they wont affect each other
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

## if we do lst1 = lst2 then the both will point to the same reference in the memory and manipulation on ,say, lst2 will affect lst1 because then its not copying is sharing the same block of array in the memory by 2 varibles ls1 and lst2.
my_foods1 = ["pizza", "falafel", "carrot cake"]

# This doesn't work:
friend_foods1 = my_foods1

my_foods1.append("cannoli")
friend_foods1.append("ice cream")

print("My favorite foods are:")
print(my_foods1)

print("\nMy friend's favorite foods are:")
print(friend_foods1)
# This syntax actually tells Python to associate the new variable friend_foods with the list that is already associated with my_foods, so now both variables point to the same list.
# As a result, when we add 'cannoli' to my_foods, it will also appear in friend_foods. Likewise 'ice cream' will appear in both lists, even though it appears to be added only to friend_foods.

## Note : we dont face such prob with strings because they are immutable.
