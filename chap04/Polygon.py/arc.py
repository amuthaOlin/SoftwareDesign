#from swampy.TurtleWorld import*
#draws an arc with radius "r" and angle "angle" 
#"t" is a turtle.

#world = TurtleWorld()
#bob = Turtle()
import math

def arc(t,r,angle):
	bob.delay=.01
	c = math.pi*r**2 
	l = c/360.0
	print t
	for i in range(angle):
		fd(t,l)
		lt(t,1)

	wait_for_user

#arc(bob,10.0,60)