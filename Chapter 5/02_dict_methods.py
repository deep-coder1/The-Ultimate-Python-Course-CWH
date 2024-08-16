marks = {
    "Deepak": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Deepak": 99, "Renuka": 100})
# print(marks)

print(marks.get("Deepak2")) # Prints None
print(marks["Deepak2"]) # Returns an error

# Output:
# \Python\The-Ultimate-Python-Course-CWH\Chapter 5> python .\02_dict_methods.py
# None
# Traceback (most recent call last):
#   File "E:\Study\Python\The-Ultimate-Python-Course-CWH\Chapter 5\02_dict_methods.py", line 15, in <module>
#     print(marks["Deepak2"]) # Returns an error
# KeyError: 'Deepak2'