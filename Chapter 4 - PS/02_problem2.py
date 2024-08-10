# 2. Write a program to accept marks of 6 students and display them in a sorted 
# manner.

marks = []

f1 = int(input("Enter Marks here: "))
marks.append(f1)
f2 = int(input("Enter Marks here: "))
marks.append(f2)
f3 = int(input("Enter Marks here: "))
marks.append(f3)
f4 = int(input("Enter Marks here: "))
marks.append(f4)
f5 = int(input("Enter Marks here: "))
marks.append(f5)
f6 = int(input("Enter Marks here: "))
marks.append(f6)

marks.sort()

print(marks)

# Output:
# \Python\The-Ultimate-Python-Course-CWH\Chapter 4 - PS> python .\02_problem2.py
# Enter Marks here: 40
# Enter Marks here: 30
# Enter Marks here: 50
# Enter Marks here: 70
# Enter Marks here: 80
# Enter Marks here: 90
# [30, 40, 50, 70, 80, 90]