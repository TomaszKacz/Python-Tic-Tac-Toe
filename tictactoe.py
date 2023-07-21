# write your code here

def game_board(rows):
    first_row = rows[0:3]
    second_row = rows[3:6]
    third_row = rows[6:9]
    print("---------")
    print("|", *first_row, "|", sep=" ")
    print("|", *second_row, "|", sep=" ")
    print("|", *third_row, "|", sep=" ")
    print("---------")


usr_input = input()
game_board(usr_input)
