def check_string(string):
    length = len(string)

    if (string[0] != '+'):
        print('False')
        return False
    
    if(string[length-1] != '+'):
        print('False')
        return False

    for i in range(1,length):
        if(string[i].isalpha()):
            if (string[i-1] != '+'):
                print('False')
                return False
            
            if ( string[i+1] != '+'):
                print('False')
                return False
           
    print('True')
    return True
            

check_string('+f+c+d+#+f+')
check_string('+d+=3=+s+')
check_string('f++d+g+8+')
check_string('+s+7+fg+r+8+')
