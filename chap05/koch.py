from swampy.TurtleWorld import*
#world = TurtleWorld()
#bob = Turtle()

import math

def koch(t, l):
	"""
	Make koch Curve with total length l and turtle t.
	"""
	t.delay=.01
	if l <= 3:
		fd(t,l)
		return
	angle = 60
	koch(t, l/3.0)
	lt(t, angle)
	koch(t, l/3.0)
	rt(t, 2*angle)
	koch(t, l/3.0)
	lt(t, angle)
	koch(t,l/3.0)
#koch(bob,500)