from swampy.TurtleWorld import*
world = TurtleWorld()
bob = Turtle()

from math import *

def gosper1(t, l):
	t.delay=.01
	if l <= 10:
		fd(t,l)
		return
	gosper1(t,l/3.0)
	rt(t, 60)
	gosper1(t,l/3.0)
	rt(t,120)
	gosper1(t,l/3.0)
	lt(t,60)
	gosper1(t,l/3.0)
	lt(t,120)
	gosper1(t,l/3.0)
	lt(t,60)
	gosper1(t,l/3.0)
gosper1(bob,500)

