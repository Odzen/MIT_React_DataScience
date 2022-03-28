def gcdRecur(a, b):
    '''
    Calculate the greatest common divisor of two positive integers
    using recursion
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    if(b==0):
        return a
    else:
        return gcdRecur(b, a%b)
