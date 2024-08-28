list_game = [0,1,1,0,1,0,0,-1,-1]
list_nums = [7,8,9,4,5,6,1,2,3]


def find_win(numpad_dict, third_row, second_row, first_row, first_col, second_col, third_col, first_diagonal, second_diagonal):
    
    #check if there is a win in the row
    # check last row
    if numpad_dict[1] + numpad_dict[2] + numpad_dict[3] == 2 and (numpad_dict[1] == 0 or numpad_dict[2] == 0 or numpad_dict[3] == 0):
        print("a win was found in the last row")
        return get_key(third_row)
    # check second row
    elif numpad_dict[4] + numpad_dict[5] + numpad_dict[6] == 2 and (numpad_dict[4] == 0 or numpad_dict[5] == 0 or numpad_dict[6] == 0):
        print("a win was found in the second row")
        return get_key(second_row)
    # check first row
    elif numpad_dict[7] + numpad_dict[8] + numpad_dict[9] == 2 and (numpad_dict[7] == 0 or numpad_dict[8] == 0 or numpad_dict[9] == 0):
        print("a win was found in the first row")
        return get_key(first_row)
    
    #check if there is a win in the column
    # check first column
    elif numpad_dict[7] + numpad_dict[4] + numpad_dict[1] == 2 and (numpad_dict[7] == 0 or numpad_dict[4] == 0 or numpad_dict[1] == 0):
        return get_key(first_col)
    # check second column
    elif numpad_dict[8] + numpad_dict[5] + numpad_dict[2] == 2 and (numpad_dict[8] == 0 or numpad_dict[5] == 0 or numpad_dict[2] == 0):
        return get_key(second_col)
    # check third column
    elif numpad_dict[9] + numpad_dict[6] + numpad_dict[3] == 2 and (numpad_dict[9] == 0 or numpad_dict[6] == 0 or numpad_dict[3] == 0):
        return get_key(third_col)
    
    # check if there is a win in the diagonal
    # check first diagonal
    elif numpad_dict[7] + numpad_dict[5] + numpad_dict[3] == 2 and (numpad_dict[7] == 0 or numpad_dict[5] == 0 or numpad_dict[3] == 0):
        return get_key(first_diagonal)
    # check second diagonal
    elif numpad_dict[9] + numpad_dict[5] + numpad_dict[1] == 2 and (numpad_dict[9] == 0 or numpad_dict[5] == 0 or numpad_dict[1] == 0):
        return get_key(second_diagonal)
            
def get_key(dict):
    for key, value in dict.items():
        if value == 0:
            return key

def avoid_loss(list_game):
    numpad_dict = {
        1: list_game[6], 
        2: list_game[7],
        3: list_game[8], 
        4: list_game[3],
        5: list_game[4],
        6: list_game[5],
        7: list_game[0],
        8: list_game[1],
        9: list_game[2]
    }
    third_row = {1: numpad_dict[1], 2: numpad_dict[2], 3: numpad_dict[3]}
    second_row = {4: numpad_dict[4], 5: numpad_dict[5], 6: numpad_dict[6]}
    first_row = {7: numpad_dict[7], 8: numpad_dict[8], 9: numpad_dict[9]}

    first_col = {7: numpad_dict[7], 4: numpad_dict[4], 1: numpad_dict[1]}
    second_col = {8: numpad_dict[8], 5: numpad_dict[5], 2: numpad_dict[2]}
    third_col = {9: numpad_dict[9], 6: numpad_dict[6], 3: numpad_dict[3]}

    first_diagonal = {7: numpad_dict[7], 5: numpad_dict[5], 3: numpad_dict[3]}
    second_diagonal = {9: numpad_dict[9], 5: numpad_dict[5], 1: numpad_dict[1]}
    if find_win(numpad_dict, third_row, second_row, first_row, first_col, second_col, third_col, first_diagonal, second_diagonal) != None:
        return find_win(numpad_dict, third_row, second_row, first_row, first_col, second_col, third_col, first_diagonal, second_diagonal)
    else:
        # check if potential loss in first row
        if numpad_dict[7] + numpad_dict[8] + numpad_dict[9] == -2 and (numpad_dict[7] == 0 or numpad_dict[8] == 0 or numpad_dict[9] == 0):
            return get_key(first_row)
        # check if potential loss in second row
        elif numpad_dict[4] + numpad_dict[5] + numpad_dict[6] == -2 and (numpad_dict[4] == 0 or numpad_dict[5] == 0 or numpad_dict[6] == 0):
            return get_key(second_row)
        # check if potential loss in third row
        elif numpad_dict[1] + numpad_dict[2] + numpad_dict[3] == -2 and (numpad_dict[1] == 0 or numpad_dict[2] == 0 or numpad_dict[3] == 0):
            return get_key(third_row)
        # check if potential loss in first column
        elif numpad_dict[7] + numpad_dict[4] + numpad_dict[1] == -2 and (numpad_dict[7] == 0 or numpad_dict[4] == 0 or numpad_dict[1] == 0):
            return get_key(first_col)
        # check if potential loss in second column
        elif numpad_dict[8] + numpad_dict[5] + numpad_dict[2] == -2 and (numpad_dict[8] == 0 or numpad_dict[5] == 0 or numpad_dict[2] == 0):
            return get_key(second_col)
        # check if potential loss in third column
        elif numpad_dict[9] + numpad_dict[6] + numpad_dict[3] == -2 and (numpad_dict[9] == 0 or numpad_dict[6] == 0 or numpad_dict[3] == 0):
            return get_key(third_col)
        # check if potential loss in first diagonal
        elif numpad_dict[7] + numpad_dict[5] + numpad_dict[3] == -2 and (numpad_dict[7] == 0 or numpad_dict[5] == 0 or numpad_dict[3] == 0):
            return get_key(first_diagonal)
        # check if potential loss in second diagonal
        elif numpad_dict[9] + numpad_dict[5] + numpad_dict[1] == -2 and (numpad_dict[9] == 0 or numpad_dict[5] == 0 or numpad_dict[1] == 0):
            return get_key(second_diagonal)

print(avoid_loss(list_game))



