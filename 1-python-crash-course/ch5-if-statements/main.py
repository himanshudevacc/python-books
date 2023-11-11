## Conditionals / Boolean Expressions
print(18 == "18")  # false

# ignoring case when checking for equality in strings returns False
car = "Audi"
print(car == "audi")  # False
print(car.lower() == "audi")  # True
# inequality check is '!='
print(2 != 1)  # True
# <,>,<=,>= other operators

## Multiple operators using "and" , "or"
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)  # True
print(age_0 >= 21 and age_1 >= 21)  # False
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)  # True
print(age_0 <= 21 or age_1 <= 21)  # False

## checking whether a value is in a list
requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toppings)  # True
print("pepperoni" in requested_toppings)  # False

## checking whehter a value is NOT in a list
banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")


## if statements
age = 19
if age >= 18:
    print("You are old enough to vote!")

## if "if" boolean is true then elifs and elses are ignored
age = 3
if age < 4:
    print("Your admission cost is $0.")  ## only this will execute
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
## but if there are multiple ifs then all booleans will be checked
age = 3
if age < 4:
    print("Your admission cost is $0.")  ## this will execute
if age < 18:
    print("Your admission cost is $25.")  ## this will also get executed
else:
    print("Your admission cost is $40.")


## Using if with lists
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

## checking that list is not empty
# When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False.
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

## Exercise
for i in range(1, 10):
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")
