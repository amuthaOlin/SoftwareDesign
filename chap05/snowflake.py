from swampy.TurtleWorld import*
world = TurtleWorld()
bob = Turtle()

import math

from koch import *

def snowflake(t):
	t.delay=.01
	koch(t,50)
	rt(t,120)
	koch(t,50)
	rt(t,120)
	koch(t,50)
snowflake(bob)