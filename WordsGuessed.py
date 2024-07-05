secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
correctGuess = ['a', 'p', 'l', 'e', 'z', 'x', 't', 'i']


def iswordguessed(secretword, lettersguessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    correctwords = 0
    for i in range(len(secretword)):
        if secretword[i] in lettersguessed:
            print(str(secretword[i]))
            correctwords += 1
    if correctwords == len(secretword):
        return True
    else:
        return False


print(iswordguessed(secretWord, lettersGuessed))
print(iswordguessed(secretWord, correctGuess))