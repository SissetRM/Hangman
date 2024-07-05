
secret_Word = 'apple'
letters_Guessed = ['e', 'i', 'k', 'p', 'r', 's']
letters_Guessed_2 = ['a', 'p', 'l', 'e']
secret_Word_2 = 'inefficacious'


def get_guessed_word(secret_word, letters_guessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    result = ['_ ']*len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            result[i] = secret_word[i]
    return "".join(result)


print(get_guessed_word(secret_Word, letters_Guessed))
print(get_guessed_word(secret_Word_2, letters_Guessed))
print(get_guessed_word(secret_Word, letters_Guessed_2))
print(get_guessed_word(secret_Word_2, letters_Guessed_2))
# '_ pp_ e'
