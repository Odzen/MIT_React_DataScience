"""
returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...
"""


def genPrimes():
    n=2
    while True:
        prime=True
        for p in range(2,n):
            if((n%p) == 0):
                prime = False
                break
        if prime:
            yield n
        n+=1
        
         
       