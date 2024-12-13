# 9. Can you change the values inside a list which is contained in set S?
# s = {8, 7, 12, "Harry", [1,2]}

s = {8, 7, 12, "Harry", [1,2]}

s[4][0] = 9

# Output:
# \Python\The-Ultimate-Python-Course-CWH\Chapter 5 - PS> python .\09_problem9.py
# Traceback (most recent call last):
#   File "E:\Study\Python\The-Ultimate-Python-Course-CWH\Chapter 5 - PS\09_problem9.py", line 4, in <module>
#     s = {8, 7, 12, "Harry", [1,2]}
# TypeError: unhashable type: 'list'