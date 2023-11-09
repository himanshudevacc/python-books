## lists - collection of items in a particular order
fruits = ["apple", "banana", "guava", "pupaya"]
print(fruits)  # ["apple", "banana", "guava", "pupaya"]
print(type(fruits))  # <class 'list'>

# accessing list elements
print(fruits[0], fruits[2].title())  # apple Guava

# using -ve integers to access elements from right
print(fruits[-1], fruits[-4])
# using f strings
print(f"I eat {fruits[2]} for the fiber.")

## Exercise 1-3
friends = ["anish", "elon", "george", "lex"]
for friend in friends:
    print(friend, end=" ")
print("\n")

## MODIFY(lists are mutable) using assignment, ADD, REMOVE elements
drinks = ["coke", "dew", "sting", "limca"]
drinks[2] = "fanta"
print(drinks)  # ['coke', 'dew', 'fanta', 'limca']

# adding elements to the end
drinks.append("thumbs up")
print(drinks)  # ['coke', 'dew', 'fanta', 'limca', 'thumbs up']

# insert element at any position using insert() method
drinks.insert(2, "sprite")
print(drinks)  # ['coke', 'dew', 'sprite', 'fanta', 'limca', 'thumbs up']

# remove elemnts from a list using del,pop(),remove()
del drinks[2]  # del is a keyword(not a method) deletes permanantly
print(drinks)  # ['coke', 'dew', 'fanta', 'limca', 'thumbs up']

# Sometimes you’ll want to use the value of an item after you remove it from a list
# because pop returns the popped value while del does not
d1 = drinks.pop()  # remove last elemnent
print(drinks)  # ['coke', 'dew', 'fanta', 'limca']
print(d1)
# pop at any position
drinks.pop(1)  ## removing "dew"
print(drinks)

# remove by value (only 1st occurence)
drinks.remove("fanta")
print(drinks)  # ['coke', 'limca']


## ORganising a list
cars = ["bmw", "baudi", "toyota", "subaru"]
cars.sort()
print(cars)  # ['baudi', 'bmw', 'subaru', 'toyota']
# reverse sort
print(cars[::-1])  # ['toyota', 'subaru', 'bmw', 'baudi']
# or
cars.sort(reverse=True)
print(cars)  # ['toyota', 'subaru', 'bmw', 'baudi']

# sort() does it permanent but to maintain the original order of a list but present it in a sorted order, you can use the sorted() function(not a method).
cars1 = ["bmw", "audi", "toyota", "subaru"]

print("Here is the original list:")
print(cars1)  # ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the sorted list:")
print(sorted(cars1))  # ['audi', 'bmw', 'subaru', 'toyota']

print("Here is the original list again:")
print(cars1)  # ['bmw', 'audi', 'toyota', 'subaru']

# Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase. So cover them into lowercase first.

## length of a list using len() function in python
print(len(cars1))  # 4
## Reversing the list
print(cars1)  # ['bmw', 'audi', 'toyota', 'subaru']
cars1.reverse()
print(cars1)  # ['subaru', 'toyota', 'audi', 'bmw']


## IndexError: list index out of range
