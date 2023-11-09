## varibles
message = "say hi to claire"
print(message)

message = "Hello Python Crash Course world!"
print(message)

## Avoiding Name Errors When Using Variables - A name error usually means we either forgot to set a variable’s value before using it, or we made a spelling mistake when entering the variable’s name.
# print(mesage) ## NameError: name 'mesage' is not defined

## Strings is a data type
# Changing Case in a String with Methods
name = "john snow"
print(name.title())  # John Snow
print(name.lower())  # john snow
print(name.upper())  # JOHN SNOW
print(name)  # john snow => strings are immutable.
# To change the string permanently, you have to assign the new value to the variable name. You cannot manipulate it.
name = name.upper()
print(name)  # JOHN SNOW

## f strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

## newlines and tabs
languages = "Languages:\n\tPython\n\tC++\n\tJS\n\tGolang"
print(languages)

## strip(),lstrip(),rstrip() => removes whitespaces
city = "  New York    "
print(city.lstrip())  # "New York    "
print(city.rstrip())  # "  New York"
print(city.strip())  # "New York"

# Removing Prefixes using str.removeprefix("prefix")
websites = [
    "https://youtube.com",
    "https://facebook.com",
    "https://yahoo.com",
    "https://shaadi.com",
    "https://google.com",
]
for i in websites:
    print(i.removeprefix("https://"), end=",")
print("\n")


# Exercise on Strings
personName = "eric smith"
messageToPerson = f"Hi {personName.title()}, hope you're doing fine."
print(messageToPerson)

author = "albert einstein"
quote = "A person who never made a mistake never tried anything new."
print(f'{author.title()} once said, "{quote}"')


## NUMBERS
# When you’re writing long numbers, you can group digits using underscores to make large numbers more readable:
moneyInCrore = 12_00_00_000

# Multiple assignments
x, y, z = 4, -3, 5  # coordintes
##python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed:
MAX_CONNECTIONS = 5000

## Dividing 2 integers give float
print(6 / 2)  # 3.0

## If you mix an integer and a float in any other operation, you’ll get a float as well:
print(f"{1+2.0},{2*3.0},{3.0**2}")  # 3.0,6.0,9.0

## you can sometimes get an arbitrary number of decimal places in your answer:
print(0.2 + 0.1)  # 0.30000000000000004
