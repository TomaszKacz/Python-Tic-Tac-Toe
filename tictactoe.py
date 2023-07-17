# write your code here
usr_input = input()
first_row = usr_input[0:3]
second_row = usr_input[3:6]
third_row = usr_input[6:9]



print("---------")
print("|", *first_row, "|", sep=" ")
print("|", *second_row, "|", sep=" ")
print("|", *third_row, "|", sep=" ")
print("---------")