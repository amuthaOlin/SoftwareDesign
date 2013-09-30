def gcd(a,b):
	"""
	Takes two numbers and finds the greatest 
	common denominator and returns it. 
	Inputs a and b should be numbers
	The output will be a number
	"""
	if a < b: 		#reverses the numbers if b 
		gcd(b,a) 	#is greater than a
	else:
		r = a%b
		if r == 0:
			print b
			return b
		else:
			gcd(b,r)

gcd(12,54)