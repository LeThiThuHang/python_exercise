def check_string(string):
    list_string = []
    length = len(string)
    w = True

    if (string[0].isalpha()):
        w = False
        print(w)
        return w
    
    if (string[length-1].isalpha()):
        w = False
        print(w)
        return w

    for index, letter in enumerate(string): 
        if letter.isalpha():
            list_string.append(index)
    
    for i in list_string:
        if (string[i-1]!='+' or string[i+1] != '+'):
            w = False
            break
    
    print(w)
    return w
            

check_string('+f+c+d+#+f+')
check_string('+d+=3=+s+')
check_string('f++d+g+8+')
check_string('+s+7+fg+r+8+')