from swampy.TurtleWorld import*

world = TurtleWorld()
bob = Turtle()


def square(t,length):
	print t
	for i in range(4):
		fd(t,length)
		lt(t)

	wait_for_user


square(bob,50)
square(bob,100)
square(bob,200)
square(bob,400)