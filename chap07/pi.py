from math import *

def calc(k):
    """
    Used to approximate pi.

    input k: integer

    return z: float

    """
    n = factorial(4*k) * (1103.0 + 26390.0*k)
    d = factorial(k)**4 * 396.0**(4.0*k)
    z = n/d
    return z
def estimate(i,x,z):
    """
    Estimates and Prints value of pi using Ramanujans method.
    Accurate to 15 digits

    input i: integer (counter)
    input x: float (estimation of pi)
    input z: float (value used in approximation)

    print: float(pi)
    return: float (pi)
    """

    b = 2 * sqrt(2.0) / 9801
    a = abs(1.0/x-pi)
    if a >= 1e-15:
        z = calc(i)+z
        i += 1
        x = b*z
        estimate(i,x,z)
    else:
        p =1.0/x
        print 1.0/x
        return p
        
def run():
    """
    Calculates the Value of Pi using Ramanujans method. 
    Accurate to 15 digits

    Return: float (pi)
    """
    return estimate(0,1,0)

run()    

