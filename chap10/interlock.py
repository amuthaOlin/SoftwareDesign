def interlock(t):
    s = []
    for i in range(len(t)):
        e = (t[i])[::2]
        o = (t[i])[1::2]
        if (e in t) & (o in t):
            s.append(t[i])
    print s


def make_word_list1():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    s = []
    t = []
    for line in open('words.txt'):

        # remove whitespace from the beginning and end
        word = line.strip()
        t.append(word)
    interlock(t)
    	

make_word_list1()

