#       auto generate buttons for each letter:
#     ::copy paste the prints to create the GUI buttons
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                   "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
row = 0
column = 0
for letter in letters:
            # create new button
            print("self.{}_button = Button(master, text='{}',"
                  " command=lambda: self.make_guess('{}'), height=2, width=3)"
                  .format(letter, letter.capitalize(), letter))
            # give the just created button a position
            print("self.{}_button.grid(row={}, column={})"
                  .format(letter, row, column))

            if column == 4:          # then start a new row for 4 other letters.
                row = row + 1        # on the next row
                column = 0           # starting at column 0
            else:
                column = column + 1  # else just add button to the existing row (not 4 yet on this row)
