from swampy.TurtleWorld import*

world = TurtleWorld()
bob = Turtle()
import math

def circle(t,r):
	bob.delay=.01
	c = math.pi*r**2 
	l = c/360.0
	print t
	for i in range(360):
		fd(t,l)
		lt(t,1)

	wait_for_user

circle(bob,10.0)