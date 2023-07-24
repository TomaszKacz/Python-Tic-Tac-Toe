# write your code here
def count_letters(game_input):
    counterx = 0
    countero = 0
    counterspace = 0
    for i in range(0, len(game_input)):
        if game_input[i] == "X":
            counterx += 1
        elif game_input[i] == "O":
            countero += 1
        elif game_input[i] == " " or game_input[i] == "_":
            counterspace += 1
    difference = abs(countero - counterx)
    return difference, counterspace
def game_board(first_row, second_row, third_row):
    print("---------")
    print("|", *first_row, "|", sep=" ")
    print("|", *second_row, "|", sep=" ")
    print("|", *third_row, "|", sep=" ")
    print("---------")


usr_input = input()
winner_x = 0
winner_o = 0
first_row = usr_input[0:3]
second_row = usr_input[3:6]
third_row = usr_input[6:9]
diffrence, whitespace = count_letters(usr_input)
game_board(first_row,second_row,third_row)
if first_row == "XXX" or second_row == "XXX" or third_row == "XXX":
    winner_x += 1
for i in range(0, 3):
    if first_row[i] == "X" and second_row[i] == "X" and third_row[i] == "X":
        winner_x += 1
for i in range(0, 3):
    if first_row[i] == "O" and second_row[i] == "O" and third_row[i] == "O":
        winner_o += 1
if first_row[2] == "X" and second_row[1] == "X" and third_row[0] == "X":
    winner_x += 1
if first_row[0] == "X" and second_row[1] == "X" and third_row[2] == "X":
    winner_x += 1
if first_row == "OOO" or second_row == "OOO" or third_row == "OOO":
    winner_o += 1
if first_row[2] == "O" and second_row[1] == "O" and third_row[0] == "O":
    winner_o += 1
if first_row[0] == "O" and second_row[1] == "O" and third_row[2] == "O":
    winner_o += 1
if winner_x > 0 and winner_o > 0 or diffrence >= 2:
    print("Impossible")
elif winner_x > 0 and winner_o == 0:
    print("X wins")
elif winner_o > 0 and winner_x == 0:
    print("O wins")
elif whitespace == 0 and winner_o == 0 and winner_x == 0:
    print("Draw")
else:
    print("Game not finished")


