def is_power(a,b):
"""
Checks if a is a power of b. 
a and b should be numbers
Function will return True if a is a power of b
"""

	if a == b:
		return True
	elif a%b == 0:
		if is_power(a/b,b):
			return True

