def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    for l in 'abcdefghijklmnopqrstuvwxyz':
        if l not in lettersGuessed:
            result += l
    return result
