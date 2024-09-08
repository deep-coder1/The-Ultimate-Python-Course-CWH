# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.

d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")
d.update({name: lang})

print(d)

# Output:
# \Python\The-Ultimate-Python-Course-CWH\Chapter 5 - PS> python .\06_problem6.py
# Enter friends name: Banti
# Enter Language name: Hindi
# Enter friends name: Adtiya
# Enter Language name: Hindi
# Enter friends name: Shubham
# Enter Language name: English
# Enter friends name: Arjun
# Enter Language name: English
# {'Banti': 'Hindi', 'Adtiya': 'Hindi', 'Shubham': 'English', 'Arjun': 'English'}