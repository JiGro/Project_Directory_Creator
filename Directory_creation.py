import os
import shutil

#1. Directory creation
def directory(path):
    try:
        os.makedirs(path)
    except:
        pass

#2. Copy Templates to new Path
def copy(path):
    files = ['C:/.../XXX_Word_template.docx', 'C:/C:/.../XXX_Excel_template.xlsx']
    for f in files:
        shutil.copy(f, path)

#3. Rename files in new path
def rename(path,old_string,new_string):
    for f in os.listdir(path):
        os.rename(os.path.join(path, f),
                  os.path.join(path, f.replace(old_string, new_string)))

#Main
#4. Input
project_name = input("What is the name of the project? (E.g. align with existing naming conventions)")
new_path = 'C:/.../'+project_name
dummy_in_string = "XXX"
#5. Functions
directory(new_path)
copy(new_path)
rename(new_path,dummy_in_string,project_name)
