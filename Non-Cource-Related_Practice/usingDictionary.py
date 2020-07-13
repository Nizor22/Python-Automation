# Creates a dictionary with the given keys and values
student = {'name': 'Nizor', 'age': 17, 'phone': '0000000000',
           'courses': ['CompSci', 'Math', 'Art']}
# Another way to create the same dictionary is to use 'dict' constructor
student2 = dict(name='Afroz', age=16, phone='99999999',
                courses=['Law', 'Math', 'Spanish'])

# Printing the dictionary
print(student)
print(student2)

# Printing a specific value by using its key
print(student['name'])
print(student2['name'])

# Adding and Modifying values for the keys in the dict.
student.update({'courses': ['CompSci', 'Math', 'Art', 'Photography'], 'gf': 'Taken'})

# Printing the amount of keys
print(f'There are {len(student)} keys in the dictionary after the update')

# Printing all the keys
print(student.keys())

# Printing all the values
print(student.values())

# Printing both keys and values
print(student.items())
print('')

# Iterating over the keys
for key in student.keys():  # not necessary to include .keys()
    print(f'Keys: {key}')
print('')

# Iterating over the values
for value in student.values():  # not necessary to include .keys()
    print(f'Values: {value}')
print('')
# Iterating and printing every key and value in the dict.
for key, value in student.items():
    print(key, value)
print('')
