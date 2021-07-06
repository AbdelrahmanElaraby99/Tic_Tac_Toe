# Game constants
GAME_ARRAY = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]]

TIC_TAC_TOE = '''
 _____  _  ____    _____  ____  ____    _____  ____  _____
/__ __\/ \/   _\  /__ __\/  _ \/   _\  /__ __\/  _ \/  __/
  / \  | ||  /      / \  | / \||  /      / \  | / \||  \  
  | |  | ||  \__    | |  | |-|||  \__    | |  | \_/||  /_ 
  \_/  \_/\____/    \_/  \_/ \|\____/    \_/  \____/\____\\
                                                          
'''
X_WINNER = '''
  _______ _                     _                         _           __    __   __
 |__   __| |                   (_)                       (_)          \ \   \ \ / /
    | |  | |__   ___  __      ___ _ __  _ __   ___ _ __   _ ___   _____\ \   \ V / 
    | |  | '_ \ / _ \ \ \ /\ / / | '_ \| '_ \ / _ \ '__| | / __| |______> >   > <  
    | |  | | | |  __/  \ V  V /| | | | | | | |  __/ |    | \__ \       / /   / . \ 
    |_|  |_| |_|\___|   \_/\_/ |_|_| |_|_| |_|\___|_|    |_|___/      /_/   /_/ \_\\
                                                                                   
                                                                                   
'''
O_WINNER = '''
  _______ _                     _                         _           __      ____  
 |__   __| |                   (_)                       (_)          \ \    / __ \ 
    | |  | |__   ___  __      ___ _ __  _ __   ___ _ __   _ ___   _____\ \  | |  | |
    | |  | '_ \ / _ \ \ \ /\ / / | '_ \| '_ \ / _ \ '__| | / __| |______> > | |  | |
    | |  | | | |  __/  \ V  V /| | | | | | | |  __/ |    | \__ \       / /  | |__| |
    |_|  |_| |_|\___|   \_/\_/ |_|_| |_|_| |_|\___|_|    |_|___/      /_/    \____/ 
                                                                                    
                                                                                    
'''
CURRENT_PLAYER = 0


# function to display relevant info at game start
def display_board_positions():
    global TIC_TAC_TOE, GAME_ARRAY
    print("### Welcome to the game ###")
    print(TIC_TAC_TOE)
    game_board_positions = [["0", "1", "2"],
                            ["3", "4", "5"],
                            ["6", "7", "8"]]
    print("## To play the game, you enter the number of the place ##")
    print("-----------")
    for row in game_board_positions:
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        print("-----------")

    display_board()


# display the game board and current player
def display_board():
    global GAME_ARRAY, CURRENT_PLAYER
    if CURRENT_PLAYER == 0:
        print("The current player: 'X'")
    else:
        print("The current player: 'O'")
    print("The current game board: ")
    print("-----------")
    for row in GAME_ARRAY:
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        print("-----------")


# insert a symbol in a position and switches the player
def update_board(position):
    global GAME_ARRAY, CURRENT_PLAYER
    row_number = position // 3
    column_number = position % 3
    if GAME_ARRAY[row_number][column_number] == " ":
        if CURRENT_PLAYER == 0:
            GAME_ARRAY[row_number][column_number] = "X"
        else:
            GAME_ARRAY[row_number][column_number] = "O"
        # Switch the player
        CURRENT_PLAYER += 1
        CURRENT_PLAYER %= 2
        return True  # True means valid entry
    else:
        print("Invalid entry, entered position is occupied.")
        return False  # False means invalid entry


# check to see if there is a winner
def check_winner():
    global GAME_ARRAY
    # check across rows
    for row in GAME_ARRAY:
        if row[0] == row[1] == row[2] == "X":
            return "X"
        elif row[0] == row[1] == row[2] == "O":
            return "O"

    # check across columns
    for i in range(3):
        if GAME_ARRAY[0][i] == GAME_ARRAY[1][i] == GAME_ARRAY[2][i] == "X":
            return "X"
        elif GAME_ARRAY[0][i] == GAME_ARRAY[1][i] == GAME_ARRAY[2][i] == "O":
            return "O"

    # check across diagonals
    if GAME_ARRAY[0][0] == GAME_ARRAY[1][1] == GAME_ARRAY[2][2] == "X":
        return "X"
    elif GAME_ARRAY[0][0] == GAME_ARRAY[1][1] == GAME_ARRAY[2][2] == "O":
        return "O"
    if GAME_ARRAY[0][2] == GAME_ARRAY[1][1] == GAME_ARRAY[2][0] == "X":
        return "X"
    elif GAME_ARRAY[0][2] == GAME_ARRAY[1][1] == GAME_ARRAY[2][0] == "O":
        return "O"
    return None


# The Game starts here
display_board_positions()
# The main loop
while True:
    place = int(input("Enter a position: "))
    updated = update_board(place)
    if updated:
        display_board()
        winner = check_winner()
        if winner == "X":
            print(X_WINNER)
            break
        elif winner == "O":
            print(O_WINNER)
            break
