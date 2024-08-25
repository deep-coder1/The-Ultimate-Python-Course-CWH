# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
s = set()
s.add(18)
s.add("18")

print(s)

# Output:
# \Python\The-Ultimate-Python-Course-CWH\Chapter 5 - PS> python .\03_problem3.py
# {'18', 18}