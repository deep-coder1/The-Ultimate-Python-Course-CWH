friends = ["Apple", "Orange", 5, 345.06, False, "Deepak", "Rohan"]
print(friends)
friends.append("Deepak")
print(friends)

l1 = [1, 34,62, 2, 6, 11]
# l1.sort()
# l1.reverse()
# l1.insert(2, 333333) # Insert 333333 such that its index in the list is 3
value = l1.pop(3)
print(value)
print(l1)

# Output:
# \Python\The-Ultimate-Python-Course-CWH\Chapter 4> python .\02_list_methods.py
# ['Apple', 'Orange', 5, 345.06, False, 'Deepak', 'Rohan']
# ['Apple', 'Orange', 5, 345.06, False, 'Deepak', 'Rohan', 'Deepak']
# 2
# [1, 34, 62, 6, 11]