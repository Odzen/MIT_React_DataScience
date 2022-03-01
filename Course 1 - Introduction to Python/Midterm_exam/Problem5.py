def keysWithValue(aDict, target):
    '''
    returns a list of keys in aDict with the value target.
    The list of keys you return should be sorted in increasing order. 
    The keys and values in aDict are both integers. 
    (If aDict does not contain the value target, you should return 
     an empty list.)
    aDict: a dictionary
    target: an integer
    '''
    results=[]
    
    keysDict=aDict.keys()
    
    for key in keysDict:
        if(aDict[key]==target):
            results.append(key)
    return sorted(results)

print(keysWithValue({1: 3, 2: 4, 3: 2, 4: 1, 5: 2, 6: 0, 8: 3, 10: 0}, 3))
