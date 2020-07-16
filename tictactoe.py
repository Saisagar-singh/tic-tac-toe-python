# write your code here
input_str = 9 * '_'
symbol = list(input_str)  # turns the string input into
print("---------")
print("|", *list(symbol)[0:3], "|", sep=' ')
print("|", *list(symbol)[3:6], "|", sep=' ')
print("|", *list(symbol)[6:9], "|", sep=' ')
print("---------")
dictionary_ = {
    "1 3": symbol[0], "2 3": symbol[1], "3 3": symbol[2],
    "1 2": symbol[3], "2 2": symbol[4], "3 2": symbol[5],
    "1 1": symbol[6], "2 1": symbol[7], "3 1": symbol[8]}
moves = 0

while moves < 9:
    user_input = input("Enter the coordinates")
    user_input_x = str(user_input)
    if user_input_x not in dictionary_:
        if int(user_input_x.replace(" ", "")) != 13 or 23 or 33 or 12 or 22 or 32 or 11 or 21 or 31:
            print("Coordinates should be from 1 to 3!")
        if type(int(user_input_x.replace(" ", ""))) == "int":
            print("You should enter numbers!")
    else:
        if dictionary_[user_input_x] == "_":
            if user_input_x == "1 3":
                if moves % 2 == 0:
                    symbol[0] = "X"
                    moves += 1
                else:
                    symbol[0] = "O"
                    moves += 1
                print("---------")
                print("|", *list(symbol)[0:3], "|", sep=' ')
                print("|", *list(symbol)[3:6], "|", sep=' ')
                print("|", *list(symbol)[6:9], "|", sep=' ')
                print("---------")
            elif user_input_x == "2 3":
                if moves % 2 == 0:
                    symbol[1] = "X"
                    moves += 1
                else:
                    symbol[1] = "O"
                    moves += 1
                print("---------")
                print("|", *list(symbol)[0:3], "|", sep=' ')
                print("|", *list(symbol)[3:6], "|", sep=' ')
                print("|", *list(symbol)[6:9], "|", sep=' ')
                print("---------")
            elif user_input_x == "3 3":
                if moves % 2 == 0:
                    symbol[2] = "X"
                    moves += 1
                else:
                    symbol[2] = "O"
                    moves += 1
                print("---------")
                print("|", *list(symbol)[0:3], "|", sep=' ')
                print("|", *list(symbol)[3:6], "|", sep=' ')
                print("|", *list(symbol)[6:9], "|", sep=' ')
                print("---------")
            elif user_input_x == "1 2":
                if moves % 2 == 0:
                    symbol[3] = "X"
                    moves += 1
                else:
                    symbol[3] = "O"
                    moves += 1
                print("---------")
                print("|", *list(symbol)[0:3], "|", sep=' ')
                print("|", *list(symbol)[3:6], "|", sep=' ')
                print("|", *list(symbol)[6:9], "|", sep=' ')
                print("---------")
            elif user_input_x == "2 2":
                if moves % 2 == 0:
                    symbol[4] = "X"
                    moves += 1
                else:
                    symbol[4] = "O"
                    moves += 1
                print("---------")
                print("|", *list(symbol)[0:3], "|", sep=' ')
                print("|", *list(symbol)[3:6], "|", sep=' ')
                print("|", *list(symbol)[6:9], "|", sep=' ')
                print("---------")
            elif user_input_x == "3 2":
                if moves % 2 == 0:
                    symbol[5] = "X"
                    moves += 1
                else:
                    symbol[5] = "O"
                    moves += 1
                print("---------")
                print("|", *list(symbol)[0:3], "|", sep=' ')
                print("|", *list(symbol)[3:6], "|", sep=' ')
                print("|", *list(symbol)[6:9], "|", sep=' ')
                print("---------")
            elif user_input_x == "1 1":
                if moves % 2 == 0:
                    symbol[6] = "X"
                    moves += 1
                else:
                    symbol[6] = "O"
                    moves += 1
                print("---------")
                print("|", *list(symbol)[0:3], "|", sep=' ')
                print("|", *list(symbol)[3:6], "|", sep=' ')
                print("|", *list(symbol)[6:9], "|", sep=' ')
                print("---------")
            elif user_input_x == "2 1":
                if moves % 2 == 0:
                    symbol[7] = "X"
                    moves += 1
                else:
                    symbol[7] = "O"
                    moves += 1
                print("---------")
                print("|", *list(symbol)[0:3], "|", sep=' ')
                print("|", *list(symbol)[3:6], "|", sep=' ')
                print("|", *list(symbol)[6:9], "|", sep=' ')
                print("---------")
            elif user_input_x == "3 1":
                if moves % 2 == 0:
                    symbol[8] = "X"
                    moves += 1
                else:
                    symbol[8] = "O"
                    moves += 1
                print("---------")
                print("|", *list(symbol)[0:3], "|", sep=' ')
                print("|", *list(symbol)[3:6], "|", sep=' ')
                print("|", *list(symbol)[6:9], "|", sep=' ')
                print("---------")
        else:
            print("This cell is occupied! Choose another one!")


def winner(bo, le):
    return ((bo[0] == le and bo[1] == le and bo[2] == le) or  # across the top

            (bo[3] == le and bo[4] == le and bo[5] == le) or  # across the middle

            (bo[6] == le and bo[7] == le and bo[8] == le) or  # across the bottom

            (bo[0] == le and bo[3] == le and bo[6] == le) or  # down the left side

            (bo[1] == le and bo[4] == le and bo[7] == le) or  # down the middle

            (bo[2] == le and bo[5] == le and bo[8] == le) or  # down the right side

            (bo[0] == le and bo[4] == le and bo[8] == le) or  # left to right diagonal

            (bo[2] == le and bo[4] == le and bo[6] == le))  # diagonal


o_num = 0
x_num = 0
for i in range(0, 9):
    if symbol[i] == "X":
        x_num += 1
    if symbol[i] == "O":
        o_num += 1
if winner(symbol, 'X') and not winner(symbol, 'O'):
    print("X wins")
elif winner(symbol, 'O') and not winner(symbol, 'X'):
    print("O wins")
elif "_" not in symbol:
    print("Draw")
