"""Checks for e's

Author: Ankeet Mutha
"""

def has_no_e(s):
    x = 0
    a = len(s)
    for i in range(0,a):
        if s[i] == 'e':
            return False
    return True


def main():
    for line in open('words.txt'):

        # remove whitespace from the beginning and end
        word = line.strip()

        # only print words without e
        if doubleletters(word):
            print word


if __name__ == '__main__':
    main()

def doubleletters(s):
    a = len(s)
    if len(s) < 6:
        return False
    for i in range(0,a-5):
        if s[i] == s[i+1]:
            if s[i+2] == s[i+3]:
                if s[i+4] == s[i+5]:
                    return True
    return False
