# import pyjokes  #module is installed; a file containing code written by others which can be used
# print(pyjokes.get_joke())

# Multiline comment:
"""
This is the beginning

"""
# Problem 1

# print('''Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
# like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
# When the blazing sun is set, and the grass with dew is wet. Then you show your little
# light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
# are.
# Then the traveler in the dark thanks you for your tiny spark. How could he see where to
# go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
# As your bright and tiny spark lights the traveler in the dark, though I know not what you
# are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are.
# ''')

# Problem 3

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hello World")
# engine.runAndWait()
# engine.runAndWait()
# engine = pyttsx3.init()
# engine.runAndWait()

# Problem 4

import os

# specify the directory path
path = "/"

# get list of files and directories
contents = os.listdir(path)

# print each item
for item in contents:
    print(item)