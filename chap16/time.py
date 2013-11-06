from datetime import *

def doubleDay(b1,b2):
    if b1 > b2:
        doubleDay(b2,b1)
    d = b2-b1
    return (b2 + d)

b1 = date(1993,12,7)
b2 = date(2000,11,16)

print doubleDay(b1,b2)

class Time(object):
    """represents time of day


    attributes: hour, minute, second
    """


time = Time()
time.hour = 11
time.minute = 59
time.second = 30

t2 = Time()
t2.hour = 12
t2.minute = 0
t2.second = 0

def print_time(t1):
    print "%2d:%2d:%2d" %(time.hour,time.minute,time.second)

def is_after(t1,t2):
    return (t1.hour,t1.minute,t1.second)>(t2.hour,t2.minute,t2.second)

#print_time(time)
#print is_after(t2,time)

if __name__ == '__main__':
    main()