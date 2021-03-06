def recurPower(base, exp):
    '''
    which computes base^exp by recursively calling itself to solve a smaller version
    of the same problem, and then multiplying the result by base to solve the
    initial problem.
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if(exp!=0):
        if(exp==1):
            return base
        else:
            return base*recurPower(base,exp-1)
    else:
        return 1
            
        