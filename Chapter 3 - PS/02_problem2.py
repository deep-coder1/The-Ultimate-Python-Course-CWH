# 2. Write a program to fill in a letter template given below with name and date.
# letter = ''' 
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Deepak").replace("<|Date|", "30 August 2024"))

# Output"
# \Python\The-Ultimate-Python-Course-CWH\Chapter 3 - PS> python .\02_problem2.py
# Dear Deepak, 
# You are selected! 
# 30 August 2024> 