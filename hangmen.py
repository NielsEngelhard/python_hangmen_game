import re
import getpass

wordGuessed = False  # indicates if the word is guessed Y/N
word_to_guess = ""   # the word to guess
words_guessed = []   # array with the letters that are already guessed
tries_done = 0       # how many tries the guesser has made
max_tries = 10       # max amount of tries


# define the word (step 1 of the whole game)
def set_word(hangmen_word):
    global word_to_guess
    word_to_guess = hangmen_word


# a guess of the guessing player (is a single letter)
def guess(user_guess):
    if not checklist(user_guess):
        print("This letter is already guessed")
    elif check_guess(user_guess):
        add_letter(user_guess)
        print("YES! this letter is in the word")
    else:
        global tries_done
        add_letter(user_guess)
        tries_done = tries_done + 1
        print("WRONG there are " + str(max_tries - tries_done) + " tries left.")
    print(hashed_word())


# returns true if it is a valid input
def checklist(to_check):
    if to_check in words_guessed:
        return False
    else:
        return True


# shows the guessed letters, if a letter is not guessed it will display a dot ( . )
def hashed_word():
    output = ""
    good_guesses = 0
    global word_to_guess
    for w in word_to_guess:
        if w in words_guessed:
            good_guesses += 1
            output = output + " " + w + " "
        else:
            output = output + " . "
    if good_guesses == len(word_to_guess):
        global wordGuessed
        wordGuessed = True
    return output


# returns true if the letter (guessed) is in the word_to_guess
def check_guess(to_check):
        if re.search(to_check, word_to_guess):
            return True
        else:
            return False


# return true if all tries are done
def end_of_game():
    if max_tries - tries_done <= 0:
        global wordGuessed
        wordGuessed = True


# add letter to the "guessed" letters list
def add_letter(letter):
    words_guessed.append(letter)


# actual program
print("What is the word of the hangmen?")
set_word(input())
while not wordGuessed:  # while the game is not over
    end_of_game()       # check max tries reached
    print("Geef een letter om te raden: ")
    user_try = input()  # input of the guesser
    guess(user_try)     # check the guess
