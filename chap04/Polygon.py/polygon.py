from swampy.TurtleWorld import*
#draws a polygon with "n" sides of length "length". 
#"t" is a turtle

bob = Turtle()


def polygon(t,length,n):
	x = 360.0/n
	print t
	for i in range(n):
		fd(t,length)
		lt(t,x)
	wait_for_user

polygon(bob,50,8)