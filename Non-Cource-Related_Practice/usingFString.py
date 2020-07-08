from datetime import datetime

# Creates a dictionary with the given keys and values
student = {'name': 'Nizor', 'age': 17, 'phone': '9293408051',
           'courses': ['CompSci', 'Math', 'Art']}

'''
 f-String = alternative for .format() method.
 Using ':' within the curly braces of f string allows us to format the content.
 Using f-String to display the sentence without any castings,
 makes it much more readable and easier to write escape characters
 and any function within a String. 
'''

print(f"Hey there! My name is {student['name']}.\nI am {student['age']} years old and I am currently taking"
      f" these courses: {student['courses']} as a high school student!\n"
      f"If you have any questions you can always call me. Here is my number {student['phone']} .")

# Using datetime library-function to store the birthday
# and display it in a nice format
birthday = datetime(2002, 12, 22)
print(f'Also my birthday is on{birthday: %B %d, %Y}.'
      f' By the way it was{birthday: %A}!')

# Using f string in a loop
for n in range(1, 11):
    print(f'The value is {n:02}')
# Zero pad formatting.
# Outputs 01, 02, 03 etc
# Changing 2 to other value will add or remove zeroes depending on your action.

# Using f string for calculations
print(f"Four times eleven is {4 * 11}")

# Using f string to round up a value of pi
pi = 3.145954354
print(f'The value of pi is {pi:.3f}')