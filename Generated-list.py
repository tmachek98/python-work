#This gives us the needed os componenets.

import os

#Created an empty list and called files which is our listed directory.

files = os.listdir()
file_dicts = []

#Used a for loop to create our dictionaries, keys, and values.

for file in files:
    file_dict = {}
    file_dict['name'] = file
    file_dict['size'] = os.path.getsize(file)
    file_dicts.append(file_dict)

print(file_dicts)

