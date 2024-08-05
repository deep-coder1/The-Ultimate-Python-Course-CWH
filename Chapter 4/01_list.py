friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0])
print(friends[1:4])

# Output:
# \Python\The-Ultimate-Python-Course-CWH\Chapter 4> python .\01_list.py
# Apple
# Grapes
# ['Orange', 5, 345.06]