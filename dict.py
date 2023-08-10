
# Methods of Creating Dictionary
# students = {}
# students = dict()



car = {
    "brand": "Mercedez Benz",
    "Model": "CLA 250",
    "Price": "16,500,000",
}

print(car["Model"]) #This prints the model of the car

car["country"] = "NG"   #Adding to the Dictionary
car["colour"] = "Red"   #This adds colour as red to the dictionary

print(car) #This prints ou[t the new car


# Accesing the dictionary value

my_dict = {
    "brand": 'Ford',
    "Model": 'Mustang',
    "Year": "1964",
    "class": "First"
}


# Method 1

model = my_dict["Model"] #Method 1 of accessng the Year
print(model)

# OR


year = my_dict.get("Year") #Methodtwo of accessing the year
print(year)


# updating dictionary

# Changing or Updating Values
updated_year = my_dict['year'] = 2022
print(updated_year)

# or

updated_year2 = my_dict.update({"year": 2023})
print(my_dict)



# Removing Items

# Method1 of removing item. The pop() Method

my_dict.pop('Model')
print(my_dict)


# Method 2 of removing Item. The popitem() method
# Note: The method will remove the last item in the dictionary
my_dict.popitem()
print(my_dict)

# Method 3. The del keyword removes the item with specified key name.
del my_dict['brand']
print(my_dict)





# DELETING DICTIONARY VALUES

# Note the Following

# dictionary.name.clear() This clear the content in the dictionary
# del dictionary This delete the entire dictionary

# Looping throught the dictionary
# Using for loop

for x in my_dict:
    print(x)  #This prints all the keys

for x in my_dict:
    print(my_dict[x]) #This prints all the values

for x in my_dict.keys():
    print(x)


# Looping through the keys and the values by using the items() method.
for x, y in my_dict.items():
    print(x, y)


# name = input("Please type ypur name: ")
# num1 = input('Enter you first number: ')
# num2 = input('Enter your second number: ')

# result = int(num1) + int(num2)

# print(result)



# num3 = input('Enter you first number: ')
# num4 = input('Enter your second number: ')

# result1 = ('Your result is: ', int(num3) - int(num4))
# result2 = ('Your result is: ', int(num3) + int(num4))
# result3 = ('Your result is: ', int(num3) / int(num4))
# result4 = ('Your result is: ', int(num3) ** int(num4))

# print(result2)

# print(type(car))

# Creating Dictionary