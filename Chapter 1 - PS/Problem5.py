# Label the program written in problem 4 with comments.

import os

# Select the directory whose content you want to list 
directory_path = '/'

# Use the os module to list the directory content 
contents = os.listdir(directory_path)

# Print the contents of the directory 
print(contents)


# Output:
#  1 - PS> python .\Problem5.py
# ['$RECYCLE.BIN', 'Backup File', 'Data', 'GitHub', 'Node Js', 'P5 Digital Solutions', 'React Next JS Projects', 'Study', 'System Volume Information', 'Tech Test']