def iterPower(base, exp):
    '''
    calculates the exponential base^exp by simply using successive multiplication. 
    For example, iterPower(base, exp) should compute bas^exp
    by multiplying base times itself exp times.
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result=1
    if(exp!=0):
        while exp>0:
            result*=base
            exp-=1
    
    return result