
def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Your code here
    vowels=['a', 'e', 'i', 'o', 'u']
    result_L=[]
    if s=='':
        result_s=''
    for letter in s:
        if letter.lower() not in vowels:
            result_L.append(letter)
    result_s=''.join(result_L)
    print(result_s)