# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 13:13:08 2017

@author: prana
"""

from sys import argv

script, filename = argv
txt = open(filename)

print "Here is your file %r :" % filename
print txt.read()
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)
print txt_again.read()
txt_again.close()

"""
Take aways -
1. to open a file, use open(name of file)
2. to read it, use obj.read()
"""





 

