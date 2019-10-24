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
def rename(path,old,project_name):
    for f in os.listdir(path):
        os.rename(os.path.join(path, f),
                  os.path.join(path, f.replace(old, project_name)))

#Main
#4. Input
project_name = input("What is the name of the project? (E.g. align with existing naming conventions)")
path = 'C:/.../'+project_name
old = "XXX"
#5. Functions
directory(path)
copy(path)
rename(path,old,project_name)
