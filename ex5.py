my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s" % my_name
print "He's %d inches tall" % my_height
print "He's %d pounds heavy" % my_weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair" % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % (my_teeth)

# this line is tricky
print "If I add %d, %d and %d then I get %d." % (my_age, my_height,my_weight, my_age + my_height + my_weight)

x = "There are %d types of people." % 10

print "I said: %r." % x
print "I said: %s." % x
