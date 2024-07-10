# 3. Install an external module and use it to perform an operation of your interest. 

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

# Output:
# I will speak this text

# Note:
# pyttsx3 2.90
# pip install pyttsx3