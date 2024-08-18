s = {1, 5, 32, 54,5, 5, 5, "Deepak"}

print(s, type(s))

s.add(566)
print(s, type(s))
s.remove(1)
print(s, type(s))

# Output:
# \Python\The-Ultimate-Python-Course-CWH\Chapter 5> python .\04_set_methods.py
# {32, 1, 5, 'Deepak', 54} <class 'set'>
# {32, 1, 5, 'Deepak', 54, 566} <class 'set'>
# {32, 5, 'Deepak', 54, 566} <class 'set'>