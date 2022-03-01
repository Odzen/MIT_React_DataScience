def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    def functionTest(x):
        k = 0
        for elem in L:
            print(k)
            k = x*k + elem
        return k
    
    return functionTest


print(general_poly([1, 2, 3, 4])(10))