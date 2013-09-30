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
    """Write a good Docstring here."""
    # TODO: fill in the body of this function
    x = len(word)/2
    n = 0
    for i in range (0,x):
        if word[i] == word[len(word)-1-i]:
            n = n +1
    if n == len(word)/2:
        return True
