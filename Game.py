from hangmen import HangmenGame
from words import Generator


game = HangmenGame()
g = Generator()
# actual program
print("Finding a word in the dictionary...")
game.set_word(g.getWordFromDictionary())
while not game.wordGuessed:  # while the game is not over
    game.end_of_game()  # check max tries reached
    print("Give letter to guess: ")
    user_try = input()  # input of the guesser
    game.guess(user_try)  # check the guess