from python_hangmen_game.hangmen import HangmenGame


game = HangmenGame()
# actual program
print("Finding a word in the dictionary...")
print(game.hashed_word())
while not game.wordGuessed:  # while the game is not over
    game.end_of_game()  # check max tries reached
    print("Give letter to guess: ")
    user_try = input()  # input of the guesser
    game.guess(user_try)  # check the guess
print("end of the game, thr word is: " + str(game.getWord))
print("press any key to exit")
input()
