def rotate_word(w,n):
"""
Rotates every character in a word forward n letters. Use only lowercase letters.

w: string
n: integer

Returns shifted word string


"""
    length = len(w)
    i = length-1
    word = ""
    for x in range(i+1):
        a = ord(w[x])
        if 97<=a<=122:
            a = a+n
            if a>122:
                a = a-26
            a=chr(a)
            word = word+a
            x=x+1
        else:
            return "Make sure input is all lowercase and contains only letters"
    return word
print rotate_word("abz",1)