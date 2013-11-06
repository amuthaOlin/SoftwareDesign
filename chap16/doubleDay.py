from datetime import *

def doubleDay(b1,b2):
    if b1 > b2:
        doubleDay(b2,b1)
    d = b2-b1
    return (b2 + d)

b1 = date(1993,12,7)
b2 = date(2000,11,16)


if __name__ == '__main__':
    print doubleDay(b1,b2)

