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

def main():
    for line in open('words.txt'):

        # remove whitespace from the beginning and end
        word = line.strip()

        # only print words without e
        if doubleletters(word):
            print word


if __name__ == '__main__':
    main()

def numbersearch():
    for i in range(100000,999995):
        s = str(i)
        if (s[2]==s[5]) & (s[3]==s[4]):
            s = str(i+1)
            if (s[1] == s[5]) & (s[2]==s[4]):
                s = str(i+2)
                if (s[1]==s[4]) & (s[2]==s[3]):
                    s = str(i+3)
                    if (s[0]==s[5]) & (s[1]==s[4]) & (s[2]==s[3]):
                        return i
    return False
    
print numbersearch()



