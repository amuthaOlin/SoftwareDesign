"""Module that provides is_palindrome.

Author of is_palindrome: Ankeet Mutha
"""

def first(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[0]


def last(word):
    """Returns the last character of a word.

    word: string

    returns: length 1 string
    """
    return word[-1]


def middle(word):
    """Returns all but the first and last character of a word.

    word: string

    returns: string
    """
    return word[1:-1]


def is_palindrome(word):
    """
    Checks if input is a palindrome.

    input word is a string
    """
    
 
    x = len(word)/2                 # divide by int 2 because middle letter doesn't matter
    n = 0
    for i in range (0,x):                   #Loop checks for palindromes
        if word[i] == word[len(word)-1-i]:  #Counter increments. 
            n = n +1
    if n == len(word)/2:
        return True
