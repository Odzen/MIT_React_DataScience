def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    dict_L1=dict()
    dict_L2=dict()
    result_tup=()
    
    for key in L1:
        try:
            dict_L1[key]+=1
        except KeyError:
            dict_L1[key]=1
    
    for key in L2:
        try:
            dict_L2[key]+=1
        except KeyError:
            dict_L2[key]=1
    
    
    if dict_L1==dict_L2 and dict_L1=={}:
        return (None, None, None)
    
    elif dict_L1==dict_L2:
        max_value=0
        for k,v in dict_L1.items():
            if max_value<v:
                max_value=v
                max_key=k
        result_tup=(max_key, max_value, type(max_key))
        return result_tup
    else:
        return False