# write your code here
def count_letters(game_input):
    counts_x = 0
    counts_o = 0
    counts_space = 0
    for i in range(0, len(game_input)):
        if game_input[i] == "X":
            counts_x += 1
        elif game_input[i] == "O":
            counts_o += 1
        elif game_input[i] == " " or game_input[i] == "_":
            counts_space += 1
    difference = abs(counts_o - counts_x)
    return difference, counts_space


def game_board(g_first_row, g_second_row, g_third_row):

    print("---------")
    print("|", *g_first_row, "|", sep=" ")
    print("|", *g_second_row, "|", sep=" ")
    print("|", *g_third_row, "|", sep=" ")
    print("---------")


usr_input = input()
winner_x = 0
winner_o = 0
first_row = usr_input[0:3]
second_row = usr_input[3:6]
third_row = usr_input[6:9]
diff, whitespace = count_letters(usr_input)
game_board(first_row, second_row, third_row)
while True:
    usr_move = input("Where u want to place X ")
    real_move = usr_move.split()
    try:
        for j in range(0, len(real_move)):
            real_move[j] = int(real_move[j])
    except ValueError:
        print("You should enter numbers!")
    else:
        if int(real_move[0]) > 3 or int(real_move[0]) < 1 or int(real_move[1]) > 3 \
                or int(real_move[1]) < 1:
            print("Coordinates should be from 1 to 3!")
        elif int(real_move[0]) == 1:
            if first_row[int(real_move[1]) - 1] != " " and \
                    first_row[int(real_move[1]) - 1] != "_":
                print("This cell is occupied! Choose another one!")
            else:
                first_row = first_row[:int(real_move[1]) - 1] + "X" + first_row[int(real_move[1]):]
                game_board(first_row, second_row, third_row)
                break
        elif int(real_move[0]) == 2:
            if second_row[int(real_move[1]) - 1] != " " and \
                    second_row[int(real_move[1]) - 1] != "_":
                print("This cell is occupied! Choose another one!")
            else:
                second_row = second_row[:int(real_move[1]) - 1] + "X" + second_row[int(real_move[1]):]
                game_board(first_row, second_row, third_row)
                break
        elif int(real_move[0]) == 3:
            if third_row[int(real_move[1]) - 1] != " " and \
                    third_row[int(real_move[1]) - 1] != "_":
                print("This cell is occupied! Choose another one!")
            else:
                third_row = third_row[:int(real_move[1]) - 1] + "X" + third_row[int(real_move[1]):]
                game_board(first_row, second_row, third_row)
                break
# if first_row == "XXX" or second_row == "XXX" or third_row == "XXX":
#     winner_x += 1
# for i in range(0, 3):
#     if first_row[i] == "X" and second_row[i] == "X" and third_row[i] == "X":
#         winner_x += 1
# for i in range(0, 3):
#     if first_row[i] == "O" and second_row[i] == "O" and third_row[i] == "O":
#         winner_o += 1
# if first_row[2] == "X" and second_row[1] == "X" and third_row[0] == "X":
#     winner_x += 1
# if first_row[0] == "X" and second_row[1] == "X" and third_row[2] == "X":
#     winner_x += 1
# if first_row == "OOO" or second_row == "OOO" or third_row == "OOO":
#     winner_o += 1
# if first_row[2] == "O" and second_row[1] == "O" and third_row[0] == "O":
#     winner_o += 1
# if first_row[0] == "O" and second_row[1] == "O" and third_row[2] == "O":
#     winner_o += 1
# if winner_x > 0 and winner_o > 0 or diff >= 2:
#     print("Impossible")
# elif winner_x > 0 and winner_o == 0:
#     print("X wins")
# elif winner_o > 0 and winner_x == 0:
#     print("O wins")
# elif whitespace == 0 and winner_o == 0 and winner_x == 0:
#     print("Draw")
# else:
#     print("Game not finished")
