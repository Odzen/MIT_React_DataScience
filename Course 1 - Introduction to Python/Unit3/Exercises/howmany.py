animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    '''
    returns the sum of the number of values associated with a dictionary
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    
    count=0
    for list in aDict.values():
        for elem in list:
            count+=1
    return count

print(how_many(animals))