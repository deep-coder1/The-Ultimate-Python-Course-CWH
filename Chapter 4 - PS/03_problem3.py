# 3. Check that a tuple type cannot be changed in python.

a = (34, 234, "Deepak")

a[2] = "Sandeep"

# \Python\The-Ultimate-Python-Course-CWH\Chapter 4 - PS\03_problem3.py", line 5, in <module>
#     a[2] = "Larry"
# TypeError: 'tuple' object does not support item assignment
# PS E:\Study\Python\The-Ultimate-Python-Course-CWH\Chapter 4 - PS> python .\03_problem3.py
# Traceback (most recent call last):
#   File "E:\Study\Python\The-Ultimate-Python-Course-CWH\Chapter 4 - PS\03_problem3.py", line 5, in <module>
#     a[2] = "Sandeep"
# TypeError: 'tuple' object does not support item assignment