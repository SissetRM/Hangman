# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


wordlist = loadWords()


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
    

def hangman(secret_word):
    """
    Takes a randomised secret word chosen by the computer.
    Runs the hangman game for the user to try to guess this secret word.
    :param secret_word:
    :return:
    """
    def target_characters(s_word):
        """
        Takes the string of the secret word, strips it of duplicate characters.
        "tc" represents the target characters the user needs to input.
        :param s_word:
        :return tc:
        """
        s_word = list(s_word)
        tc = []
        for i in range(len(s_word)):
            if s_word[i] not in tc:
                tc.append(s_word[i])
        return tc

    def guessing(sw):
        """
        loops while the user is trying to guess the word.
        Breaks when all the characters are guessed.
        :param sw:
        :return:
        """
        guesses = 8
        letters_guessed = []
        available_letters = get_available_letters(letters_guessed)
        target = target_characters(sw)
        correct_guesses = []
        i = 0  # counts number of iterations though the while loop.
        while True:
            print("-----------")
            print("You have " + str(guesses) + " guesses left.")
            print("Available Letters: " + available_letters)
            while True:
                user_guess = input("Please guess a letter: ")
                if len(user_guess) > 1:
                    print("Please only choose one character.")
                else:
                    letters_guessed.append(user_guess)
                    break
            if user_guess in available_letters:
                available_letters = get_available_letters(letters_guessed)
                if user_guess in sw:
                    print("Good guess: " + get_guessed_word(sw, letters_guessed))
                    correct_guesses.append(letters_guessed[-1])
                    print(letters_guessed[-1])
                else:
                    print("Oops! That letter is not in my word: "
                          + get_guessed_word(sw, letters_guessed))
                    guesses -= 1
            else:
                print("Oops! You've already guessed that letter: "
                      + get_guessed_word(sw, letters_guessed))
                i -= 1
            if "".join(sorted(target)) == "".join(sorted(correct_guesses)):
                print("-----------")
                print("congratulations, you won!")
                break
            if guesses == 0:
                print("Sorry, you ran out of guesses. The word was "
                      + sw + ".")
                break
            i += 1

    print("Welcome to the Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    guessing(secret_word)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
