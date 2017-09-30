# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 12:24:26 2017

@author: pranay
"""

"""
Functions do 3 things - 
1. They name pieces of code the way variables name string and numbers
2. They take arguments the way scripts takes argv
3. Using #1 and #2, they let you make your mini scripts of commands
"""

# This one like your scripts with argv
def print_two(*args):
    arg1,arg2 = args
    print "arg1 : %r, arg2 : %r" % (arg1,arg2)
    
def print_two_again(arg1,arg2):
    print "arg1 : %r, arg2 : %r" % (arg1,arg2)

def print_one(arg1):
    print "arg1 : %r" % arg1

def print_none():
    print "I get nothing" 

print_two("Pranay","Mehta")
print_two_again("Repeating","again")
print_one("First")
print_none()

