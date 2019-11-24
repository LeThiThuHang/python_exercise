def enumerate(list,n):
    """ crete a tuple """
    enumerate_list = ()

    for x in list:
        new_typle =(n,x)
        """ to add a tuple into a typle, need to use this """
        enumerate_list = enumerate_list + (new_typle,)
        n +=  1
   
    print(enumerate_list)
    return enumerate_list


""" 
enumerate(['a','b','c'],0)
enumerate(['a','b','c'],2)
 """

def filter_function(function, seq):
    filter_list = []
    for x in seq:
        if function(x):
            filter_list.append(x)
    print(filter_list)
    return filter_list

# TESTING filter_function

# step 1: build the function that filters vowels 
def fun(variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True
    else: 
        return False
  
  
# step 2: variable sequence 
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 
  
# step 3: use the filter function
""" filtered = filter_function(fun, sequence)  """

def map_function(function, seq):
    #can be a list, a string, a stuple, or a range
    map_seq = []
    for x in seq:
        new_x = function(x)
        map_seq.append(new_x)
    print(map_seq)
    return map_seq

# TESTING map_function

# step 1: build the function use in map
def addition(n): 
    return n + n 
  
# step 2, testing the map_function
numbers = (1, 2, 3, 4) 
""" result = map_function(addition, numbers)  """



def lim_range(start, stop, step = 1):
    output_list = []
    value = start
    while (value < stop):
        output_list.append(value)
        value += step
    print(output_list)
    return output_list

""" lim_range(-1,4,2)
lim_range(0,4)
lim_range(2,13,3) """


def set_function(aList):
    set_aList = set()
    for x in aList:
        if (x in set_aList) == False:
            set_aList.add(x)
    print(set_aList)
    return set_aList

""" set_function([0,1,1,23,4,3,4]) """


#for the aList array, first run, compare the two continuous number, if find the one before is larger, than swap
#then repeat the whole process again for the new aList array 
#until the maximum and minimum number is right

def sorted(aList):
    length = len(aList)-1
    #this is the number of times that you should sort the array
    times = len(aList)*(len(aList)-1)/2
    j=0
    #this not going to work in case the array has the min and max number repeatedly
    while(j <= times):
        print(j)
        j = j+1
        for i in range(length):
            if aList[i] > aList[i+1]:
                temporary = aList[i+1]
                aList[i+1] = aList[i]
                aList[i] = temporary
                print(aList)
                break

    print(aList)
    return aList

sorted([4,1,3,2,4,1,23,4,5,67,89,1])
sorted([4,1,3])


def rounded(number):


    
    

