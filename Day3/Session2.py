# Modules - every single python file ending with .py
# all functions, variables, program\code
import os, time, math, sys, csv, html, pickle, datetime
print(os.getcwd())
#time.sleep(5)
print('completed')
print(math.sin(0), math.cos(0))
print(sys.path)
print(dir(sys))
print(help(sys.exit))

# Package - a directory where a multiple modules exists, __init__.py
from html import entities as en
from html.parser import unescape
from html import *

unescape(s='va')
print(en.html5)

# Create a python package, automatically create __init__.py
# Create your own module and add functions there
# Try importing its functions into your another module
import mypackage.mymodule as mymod
from mypackage import *
print(pi)
print(litre)
print(next(subtr()))
print(mymod.addition(50, 10))
sys.path.append('c:\\Gaurav\Python')
print(sys.path)