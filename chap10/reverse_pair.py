def reverse_pair(t):
    s = []
    for i in range(len(t)):
        if reverse(t[i]) in t:
            s.append(t[i])
    print s


def reverse(r):
    return r[::-1]

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
    reverse_pair(t)
    	

make_word_list1()

