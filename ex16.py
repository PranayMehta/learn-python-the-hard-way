# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 22:47:11 2017

@author: prana


• close—Closes the file. Like File- >Save.. in your editor.
• read—Reads the contents of the fi le. You can assign the result to a variable.
• readline—Reads just one line of a text file.
• truncate—Empties the file. Watch out if you care about the file.
• write(stuff)—Writes stuff to the file.
"""       

from sys import argv
script, filename = argv

print argv

print " We are going to erase %r" % filename
print "If you dont want that, HIT CTRL-C (^C)."
print "If you dont want that, HIT RETURN."

raw_input("? ")


print " Opening the file ..... "
target = open(filename, 'w')


print " Truncating the file, Good bye"
target.truncate()

print "Now, I am going to ask you three lines"

line1 = raw_input("line 1 : ")
line2 = raw_input("line 2 : ")
line3 = raw_input("line 3 : ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it"
target.close()





