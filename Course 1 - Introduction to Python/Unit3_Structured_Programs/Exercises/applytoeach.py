testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def turnToPositive(n):
    if(n<0):
        n*=-1
    return n

applyToEach(testList, turnToPositive)

def sumOne(n):
    n+=1
    return n

applyToEach(testList, sumOne)

def square(n):
    n**=2
    return n

applyToEach(testList, square)