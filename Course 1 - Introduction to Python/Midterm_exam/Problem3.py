def myLog(x, b):
    '''
    computes the logarithm of a number x relative to a base b.
    
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    counterExp=0
    result=0
    while(result<=x):
        counterExp+=1
        if(result==x):
            counterExp-=1
            return counterExp
        result=b**counterExp
    return counterExp-1

print(myLog(28, 3))