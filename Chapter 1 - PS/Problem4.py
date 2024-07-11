''' 4. Write a python program to print the contents of a directory using the os module.
Search online for the function which does that. '''


# AI code from Chat GPT

# import os

# def list_directory_contents(path='.'):
#     try:
#         # Get the list of files and directories in the specified directory
#         entries = os.listdir(path)
#         print(f"Contents of '{path}':")
        
#         # Iterate and print each entry
#         for entry in entries:
#             print(entry)
#     except FileNotFoundError:
#         print(f"The directory '{path}' does not exist.")
#     except PermissionError:
#         print(f"Permission denied to access '{path}'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Specify the directory path here
# directory_path = '.'  # Current directory
# list_directory_contents(directory_path)

# Output:
#  1 - PS> python .\Problem4.py
# Contents of '.':
# Problem1.py
# Problem2.py
# Problem3.py
# Problem4.py



# AI code from Google Bard (Gemini)

import os

# Get the directory path (replace with your desired path)
directory_path = "/"

# Use os.listdir() to get a list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print("Contents of", directory_path, ":")
for item in contents:
    print(item)

# Output:
#  1 - PS> python .\Problem4.py
# Contents of / :
# $RECYCLE.BIN
# Backup File
# Data
# GitHub
# Node Js
# P5 Digital Solutions
# React Next JS Projects
# Study
# System Volume Information
# Tech Test