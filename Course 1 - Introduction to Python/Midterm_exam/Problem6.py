def gcd(a, b):
    """
    Calculates the greatest common divisor of two positive integers. 
    The gcd of two or more integers, when at least one of them is not zero, 
    is the largest positive integer that divides the numbers without a remainder.
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    
    if(b==0):
        return a
    else:
        return gcd(b, a % b)


print(gcd(20,12))