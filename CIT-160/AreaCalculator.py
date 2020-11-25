print "Welcome! I will help you calculate the area of the shape you choose"
print "What I need next is for you to enter 'C' for circle, 'T' for triangle, or 'R' for rectangle: "
theShape = raw_input("Please type 'C', 'T', or 'R'")
if theShape == "C":
	print "You want the area of a Circle, correct?"
elif theShape == "T":
	print "You want the area of a Triangle, right?"
elif theShape == "R":
	print "You want the area of a Rectangle, yes?"
else:
	print "You did not enter a valid letter"