def isIn(char,aStr):
    '''
    use the idea of bisection search to determine if a character is in a string, 
    so long as the string is sorted in alphabetical order.
    
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    
    if(len(aStr)==0):
        return False
    if(len(aStr)==1):
        if(char==aStr):
            return True
        
    middleIndex = len(aStr)//2
    middleChar = aStr[middleIndex]
    
    if(char==middleChar):
        return True
    elif(char<middleChar):
        return isIn(char,aStr[:middleIndex])
    else:
        return isIn(char,aStr[middleIndex+1:])
