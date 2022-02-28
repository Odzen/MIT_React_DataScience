def gcdIter(a, b):
    '''
    The greatest common divisor of two positive integers is the
    largest integer that divides each of them without remainder. 
    For example,

    gcd(2, 12) = 2

    gcd(6, 12) = 6

    gcd(9, 12) = 3

    gcd(17, 12) = 1
    
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    testValue=0
    
    if(a<b):
        testValue=a
    else:
        testValue=b
    
    while(testValue>0):
        if(a%testValue==0 and b%testValue==0):
            break;
        testValue-=1
    return testValue