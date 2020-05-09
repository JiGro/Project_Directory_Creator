# CREATING NEW PROJECT DIRECTORY FOR RENAMED TEMPLATES BASED ON DEFINED NAMING CONVENTION

![Logo of the project](https://cdn.pixabay.com/photo/2016/11/22/19/24/archive-1850170_960_720.jpg)

### PROJECT INTENTION
**Who does not know the struggle?** You have (project) templates, which you must use for certain project types, but then you also have to save them in a distinct location, following a naming convention (if so) and renaming the files too! The more projects there is, the more daunting is the task.

This is why I came up with this little .py script to not just save time, but also perfectly organize my project folder structure. Before starting a certain project type, I just set the project name as well as the naming convention and the script does the rest for me.

***
🛑🛑🛑 **DISCLAIMER** 🛑🛑🛑
Prior to executing the script adapt the following code lines: 

1.) Update the placeholder template _files_ paths but make sure the templates contain a placeholder so that the project name can be inserted.
```shell
#2. Copy Templates to new Path
def copy(path):
    files = ['C:/.../XXX_Word_template.docx', 'C:/C:/.../XXX_Excel_template.xlsx']
    for f in files:
        shutil.copy(f, path)
```

2.) Then, define the target directory under _new_path_ and make sure the _dummy_in_string_ matches the dummy from step 1.) 
```shell
#4. Input
project_name = input("What is the name of the project? (E.g. align with existing naming conventions)")
new_path = 'C:/.../'+project_name
dummy_in_string = "XXX"
```

Now, after starting the script, insert the desired _project_name_ and let the script work its magic!
