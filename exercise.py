# Write a python program to create a new dictionary by extracting the mentioned keys from the below dictionary
sample_dict = {
    'name': "Kelly",
    'age': 25,
    'salary': 8000,
    'city': "New York"
}

new_dictinary = {
    'name': sample_dict['name'],
    'salary': sample_dict['salary']
}

print(new_dictinary)


