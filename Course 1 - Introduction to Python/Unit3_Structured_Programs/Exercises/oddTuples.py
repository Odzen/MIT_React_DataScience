def oddTuples(aTup):
    '''
    
    takes a tuple as input, and returns a new tuple as output, 
    where every other element of the input tuple is copied, 
    starting with the first one. So if test is the tuple 
    ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples 
    on this input would return the tuple ('I', 'a', 'tuple').
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    tupResult = ()
    for element in range(0,len(aTup),2):
        tupResult+=(aTup[element],)
    
    return tupResult;