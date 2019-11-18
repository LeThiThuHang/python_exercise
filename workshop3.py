""" pseudo code:
    loop through every letter in the string
    check if the letter is equal to char
    if equal then return True
    after the for loop, if none of the letter resemble the char, return False
"""

def is_in(char,string):
    for i in range(len(string)):
        if (char == string[i]):
            print(True)
            return True
    
    print(False)
    return False
    
is_in("a","apple")
is_in("a","bullshit")


""" pseudo code:
    loop through every element in the seq
    check if the next element is larger than the previous element 
    if not, then return False

    after the for loop, if the whole seq has the next elements always larger than previous element , return True
"""

def is_sorted(seq):
    for i in range(len(seq)-1):
        if (seq[i] > seq[i+1]):
            print(False)
            return False
    
    print(True)
    return True

is_sorted([1,2,3])
is_sorted([1,3,2])

is_sorted(['a','b','c'])
is_sorted(['a','c','b'])

is_sorted('abc')
is_sorted('bac')


