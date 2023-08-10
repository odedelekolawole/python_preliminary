# print(type("Welcome to Backend"))'.;]'
# print(type(2))


# firstname = input("Enter your first name: ")
# lastname = input("input your lastname: ")
# fullname = print(f'My full name is {firstname}, {lastname}')


# print(2 + 2)
# print(2 - 2)
# print(2 * 2)
# print(2 / 2)
# print(2 // 2)
# print(2 ** 2)
# print(5 // 2)
# print(5 % 2)

# Accessing Elemnt of a String

# name = "Princewill"

# print(name[1])

# # Negative Indexing:

# print(name[-1])

# # Slicing
# # Slicing start from 0 to n-1

# greet = 'Hello'

# print(greet[1:4]) 


# # Multi-line String

# message = """ hello , i am Prosper 
# I am teaching python with Django"""


# print(message[0:15])


# # STRING OPERATOR

# # Comparing Operation 
# a = 5
# print(a == 5)


# name = "SAMUEL"

# name2 = "SAMUEL"

# print(name = name2)

# Concatenation

first_name = "Kolawole"
last_name = "Odedele"

print(first_name + ' ' + last_name)

# Lrength of a string

# print(len(first_name) + len(last_name))

# String membership

print("i" in first_name)

new1 = last_name.lower()
new2 = last_name.upper()

print(new1)
print(new2)

name = 'ayodeji'
sur = 'emmanuel'

new3 = name.capitalize()
print(new3)

print(sur.count('mm'))

# Iteration

for letter in sur:
    print(letter[::-1])