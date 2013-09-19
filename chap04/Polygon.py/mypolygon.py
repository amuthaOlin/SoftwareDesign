from swampy.TurtleWorld import*

world = TurtleWorld()
bob = Turtle()


def square(t):
	print t
	for i in range(4):
		fd(t,100)
		lt(t)

	wait_for_user

square(bob)