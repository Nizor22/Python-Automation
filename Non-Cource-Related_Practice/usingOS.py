import os
'''
@author Nizor
@date 5/31/20
The script uses cdm commands to look up all the files in
'Organizing Directories' folder and output every
folder and files in the given path. 
'''
PATH = "C:/Users/megan/Desktop/Courses/Python_Automation/MyFiles/Organizing directories"

# '% s' is a converter, but idk how here it is a place-holder.
#  It is being replaced by the content of the path variable.
#  The single quotation just server to show the quotes on the output.
print("Files and directories in '% s':" % PATH)

#  For a given directory finds every folder or a file and
#  outputs its name.
for entry in os.scandir(PATH):
    if entry.is_dir() or entry.is_file():
        print(entry.name)