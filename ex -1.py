Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #!/usr/bin/env python37
>>> #line above useful for Unix based
>>> #operating systems like Linux and OSX
>>> 
>>> #ex-1.py
>>> 
>>> print("\nPython College")

Python College
>>> print("777 Serpentine Drive")
777 Serpentine Drive
>>> Message - "A fun place to code!\n"
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    Message - "A fun place to code!\n"
NameError: name 'Message' is not defined
>>> Message = "A fun place to code"
>>> print("message")
message
>>> 
>>> print("Message")
Message
>>> 
>>> pups = 2
>>> 
>>> kittens = 5
>>> 
>>> pets = pups + kittens
>>> 
>>> print("I have this many pets:", pets)
I have this many pets: 7
>>> 
>>> print("\nI have{} pets.".format(pets))

Ihave7 pets.
