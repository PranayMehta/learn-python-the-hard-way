x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know  %s and those who %s" % (binary, do_not)

print x
print y

print "I said: %r." %x
print "I also said:'%s'." % y # THIS will print "y" in single quotes

hilarious = False
joke_evaluation = "Isn't that joke funny?! %r"

print joke_evaluation % hilarious
w = "This is the left side of..."
e = "a string with a right side."

print w + e

# %r is raw data format, used for debugging
