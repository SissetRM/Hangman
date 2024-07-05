def get_available_letters(letters_guessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    alph = list("abcdefghijklmnopqrstuvwxyz")
    for i in range(len(letters_guessed)):
        if letters_guessed[i] in alph:
            alph.remove(letters_guessed[i])
    return "".join(alph)


lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(get_available_letters(lettersGuessed))
lettersGuessed2 = list('abcdfghjlmnoqtuvwxyz')
print(get_available_letters(lettersGuessed2))
