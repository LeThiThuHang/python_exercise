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
    
""" is_in("a","apple")
is_in("a","bullshit") """


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

""" is_sorted([1,2,3])
is_sorted([1,3,2])

is_sorted(['a','b','c'])
is_sorted(['a','c','b'])

is_sorted('abc')
is_sorted('bac') """

def abs(x):  
    if x > 0: 
        abs_number = x
    else:
        abs_number = -x

    print(abs_number)
    return abs_number

""" abs(-54)
abs(-84.5) """

def all(aList):
    for item in aList:
        if(item != True):
            print(False)
            return False
    print(True)
    return True

""" all([0,1,1])
all([True,True,True,1])
all([True,False,True])
 """

def any(aList):
    for item in aList:
        if item:
            print('True')
            return True
    print('False')
    return False

""" any([0,1])
any([False,False])
any([True,False]) """

def max(aList):
    max_number = aList[0]
    for number in aList:
        if number > max_number:
            max_number = number
    print(max_number)
    return max_number

""" max([0,4,5,8,10,3])
max([0,4,11,8,10,3]) """

def min(aList):
    min_number = aList[0]
    for number in aList:
        if number < min_number:
            min_number = number
    print(min_number)
    return min_number

""" min([4,5,8,10,3])
min([1,4,11,8,10,3]) """

def reversed(list):
    length = len(list) -1
    reserve_list = []

    for i in range(length,-1, -1):
        reserve_list.append(list[i])

    print(reserve_list)
    return reserve_list

""" reversed([0,1,3,2])
reversed(['a',1,'b',2])
 """

def sum(aList):
    sum = 0
    for i in aList:
        """  this is to check if i is a number or not, any Multiply the object by zero. 
        Any number times zero is zero. Any other result means that the object is not a number 
        (including exceptions) """
        if (0 == 0*i):
            sum += i

    print(sum)
    return sum

""" sum([0,1,3,2])
sum(['a',1,'b',2])
 """



