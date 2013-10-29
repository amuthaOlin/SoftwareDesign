"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import string
import random
markov = {}

def process_file(filename, skip_header=True):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    Returns: map from each word to the number of times it appears.
    """
    
    fp = file(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:

        process_line(line, markov)
    return markov


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_line(line, markov):
    line = line.replace('-', ' ')
    words = line.split()
    for i in range(len(words)-2):
        word1 = words[i]
        word2 = words[i+1]
        prefix = word1+' '+word2
        suffix = words[i+2]
        if markov.get(prefix) == None:
            t1 = []
            markov[prefix] = t1
            (markov.get(prefix)).append(suffix)
        else:
            markov.get(prefix).append(suffix)


def analysis(markov):
    statement = []
    s = random.choice(markov.keys()).split()
    statement.extend(s)
    
    for i in range(1,100):
        try:
            a = (random.choice(markov.get(statement[i-1]+' '+statement[i]))).split()
        except TypeError:
            a = random.choice(markov.keys()).split()
        
        statement.extend(a)
        
    return statement





if __name__ == '__main__':
    markov = process_file('emma.txt', skip_header=True)
    print analysis(markov)

