# screenshots_organizer

Automate all screenshots to be in a folder on your desktop **cough cough mac's current system is absolute horror**

The following program is meant to run everytime a screenshot is taken. Then, it prompts the user to rename the screenshot to something meaningful and adds it to a folder called Screenshots in your desktop. This gets rid of the cluster of screenshots that accumulate on your desktop and gives it an actual name instead of something like "Screenshot 2024-06-13 at 2.44.37 PM.png"

# get a virtual environment

```
$ python3 -m venv /path/to/project/name_of_env
$ source /path/to/project/name_of_env/bin/activate
```

# for Pillow import

```
$ pip install Pillow
```

# inside code

replace the sss_direcrory_path and desktop_directory_path with your specific paths
