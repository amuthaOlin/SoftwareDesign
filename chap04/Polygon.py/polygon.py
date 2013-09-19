from swampy.TurtleWorld import*

world = TurtleWorld()
bob = Turtle()


def polygon(t,length,n):
	x = 360.0/n
	print t
	for i in range(n):
		fd(t,length)
		lt(t,x)

	wait_for_user

polygon(bob,50,8)