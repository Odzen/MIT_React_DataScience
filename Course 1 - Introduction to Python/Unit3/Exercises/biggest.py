def biggest(aDict):
    '''
    returns the key corresponding to the entry with the largest
    number of values associated with it. If there is more 
    than one such entry, return any one of the matching keys.
    
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if (len(aDict.values())==0):
        return None
    else:
        biggest=0
        for list in aDict.values():
            l=len(list)
            if(l>biggest):
                biggest=l
        for key in aDict.keys():
            lValue=len(aDict[key])
            if(lValue==biggest):
                return key

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))