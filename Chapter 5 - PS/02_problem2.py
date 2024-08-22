# 2. Write a program to input eight numbers from the user and display all the unique 
# numbers (once).

s = set()
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  
n = input("Enter number: ")
s.add(int(n))  

print(s)

# Output:
# \Python\The-Ultimate-Python-Course-CWH\Chapter 5 - PS> python .\02_problem2.py
# Enter number: 8
# Enter number: 5
# Enter number: 4
# Enter number: 9
# Enter number: 12
# Enter number: 47
# Enter number: 52
# Enter number: 13
# {4, 5, 8, 9, 12, 13, 47, 52}