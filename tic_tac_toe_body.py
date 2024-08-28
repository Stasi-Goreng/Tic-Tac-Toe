
import numpy as np
import pandas as pd
import avoid_loss as avoid

class game_functions:
    def __init__(self):
        self.upper_left_empty = """               O
               O
               O
               O
               O
oooooooooooooooo"""
        self.upper_left_empty = self.upper_left_empty.split('\n')
        self.upper_left_x = """      x   x    O
       x x     O
        x      O
       x x     O
      x   x    O
oooooooooooooooo"""
        self.upper_left_x = self.upper_left_x.split('\n')
        self.upper_left_o = """        oo     O
       o  o    O
      o    o   O
       o  o    O
        oo     O
oooooooooooooooo"""
        self.upper_left_o = self.upper_left_o.split('\n')
        self.upper_middle_empty = """           O
           O
           O
           O
           O
oooooooooooo"""
        self.upper_middle_empty = self.upper_middle_empty.split('\n')
        self.upper_middle_x = """   x   x   O
    x x    O
     x     O
    x x    O
   x   x   O
oooooooooooo"""
        self.upper_middle_x = self.upper_middle_x.split('\n')
        self.upper_middle_o = """     oo    O
    o  o   O
   o    o  O
    o  o   O
     oo    O
oooooooooooo"""
        self.upper_middle_o = self.upper_middle_o.split('\n')
        self.upper_right_empty = """



        
ooooooooooooooo"""
        self.upper_right_empty = self.upper_right_empty.split('\n')
        self.upper_right_o = """     oo     
    o  o    
   o    o   
    o  o    
     oo     
oooooooooooooooo"""
        self.upper_right_o = self.upper_right_o.split('\n')
        self.upper_right_x = """    x   x
     x x
      x
     x x
    x   x
oooooooooooooooo"""
        self.upper_right_x = self.upper_right_x.split('\n')
        self.middle_left_empty = """               0
               0
               0
               0
               0
oooooooooooooooo"""
        self.middle_left_empty = self.middle_left_empty.split('\n')
        self.middle_left_x = """      x   x    0
       x x     0
        x      0
       x x     0
      x   x    0
oooooooooooooooo"""
        self.middle_left_x = self.middle_left_x.split('\n')
        self.middle_left_o = """        oo     0
       o  o    0
      0    o   0
       0  0    0
        00     0
oooooooooooooooo"""
        self.middle_left_o = self.middle_left_o.split('\n')
        self.middle_middle_empty = """           O
           O
           O
           O
           O
oooooooooooo"""
        self.middle_middle_empty = self.middle_middle_empty.split('\n')
        self.middle_middle_x = """   x   x   O
    x x    O
     x     O
    x x    O
   x   x   O
oooooooooooo"""
        self.middle_middle_x = self.middle_middle_x.split('\n')
        self.middle_middle_o = """    oo     O
   o  o    O
  o    o   O
   o  o    O
    oo     O
oooooooooooo"""
        self.middle_middle_o = self.middle_middle_o.split('\n')
        self.middle_right_empty = """



        
ooooooooooooooo"""
        self.middle_right_empty = self.middle_right_empty.split('\n')
        self.middle_right_x = """    x   x 
     x x   
      x   
     x x  
    x   x 
oooooooooooooooo
        """
        self.middle_right_x = self.middle_right_x.split('\n')
        self.middle_right_o ="""      oo        
     o  o
    o    o
     o  o     
      oo 
oooooooooooooooo"""
        self.middle_right_o = self.middle_right_o.split('\n')
        self.lower_left_empty = """               O
               O
               O
               O
               O
"""
        self.lower_left_empty = self.lower_left_empty.split('\n')
        self.lower_left_x = """      x   x    O
       x x     O
        x      O
       x x     O
      x   x    O
"""
        self.lower_left_x = self.lower_left_x.split('\n')
        self.lower_left_o = """        oo     O
       o  o    O
      0    o   O
       0  0    O
        00     O
"""
        self.lower_left_o = self.lower_left_o.split('\n')
        self.lower_middle_empty = """           O
           O
           O
           O
           O
           """
        self.lower_middle_empty = self.lower_middle_empty.split('\n')
        self.lower_middle_x = """   x   x   O
    x x    O
     x     O
    x x    O
   x   x   O
           """
        self.lower_middle_x = self.lower_middle_x.split('\n')
        self.lower_middle_o = """    oo     O
   o  o    O
  o    o   O
   o  o    O
    oo     O
           """
        self.lower_middle_o = self.lower_middle_o.split('\n')
        self.lower_right_empty = """



        
"""
        self.lower_right_empty = self.lower_right_empty.split('\n')
        self.lower_right_x = """    x   x 
     x x   
      x   
     x x  
    x   x
"""
        self.lower_right_x = self.lower_right_x.split('\n')
        self.lower_right_o = """      oo        
     o  o
    o    o
     o  o     
      oo
"""
        self.lower_right_o = self.lower_right_o.split('\n')

    def input_valid(self,input,game_status):
        row = (8 - (input - 1)) // 3
        col = (input - 1) % 3
        if game_status[row][col] == '' and not game_status[row][col] == 'x' and not game_status[row][col] == 'o':
            return True
        else:
            return False

    def convert_to_ai_symbols(self, game_status):
        conv_mat_flat = list(np.array(game_status).flatten())
        convert_list = lambda x: -1 if x == 'x' else 1 if x == 'o' else 0
        for i in range(len(conv_mat_flat)):
            conv_mat_flat[i] = convert_list(conv_mat_flat[i])
        return conv_mat_flat

    def ai_move(self, game_status, num_turns, model_win_move_0, model_win_move_1, model_win_move_2, model_win_move_3, model_win_move_4, model_win_move_5, model_win_move_6, model_win_move_7, model_win_move_8, model_draw):
        #convert matrix filled with 'x' and 'o' into a list of -1 ,0 and 1
        game_stat_ai = self.convert_to_ai_symbols(game_status)
        current_df = pd.DataFrame([game_stat_ai], columns=['7','8','9','4','5','6','1','2','3'])
        avoid_loss = avoid.avoid_loss(game_stat_ai)
        if avoid_loss == None:
            if num_turns == 0:
                prediction = model_win_move_0.predict(current_df)
                while not self.input_valid(prediction[0], game_status):
                    prediction = model_draw.predict(current_df)
                return prediction[0]
            elif num_turns == 1:
                prediction = model_win_move_1.predict(current_df)
                while not self.input_valid(prediction[0], game_status):
                    prediction = model_draw.predict(current_df)
                return prediction[0]
            elif num_turns == 2:
                prediction = model_win_move_2.predict(current_df)
                while not self.input_valid(prediction[0], game_status):
                    prediction = model_draw.predict(current_df)
                return prediction[0]
            elif num_turns == 3:
                prediction = model_win_move_3.predict(current_df)
                while not self.input_valid(prediction[0], game_status):
                    prediction = model_draw.predict(current_df)
                return prediction[0]
            elif num_turns == 4:
                prediction = model_win_move_4.predict(current_df)
                while not self.input_valid(prediction[0], game_status):
                    prediction = model_draw.predict(current_df)
                return prediction[0]
            elif num_turns == 5:
                prediction = model_win_move_5.predict(current_df)
                while not self.input_valid(prediction[0], game_status):
                    prediction = model_draw.predict(current_df)
                return prediction[0]
            elif num_turns == 6:
                prediction = model_win_move_6.predict(current_df)
                while not self.input_valid(prediction[0], game_status):
                    prediction = model_draw.predict(current_df)
                return prediction[0]
            elif num_turns == 7:
                prediction = model_win_move_7.predict(current_df)
                while not self.input_valid(prediction[0], game_status):
                    prediction = model_draw.predict(current_df)
                return prediction[0]
            elif num_turns == 8:
                prediction = model_win_move_8.predict(current_df)
                while not self.input_valid(prediction[0], game_status):
                    prediction = model_draw.predict(current_df)
                return prediction[0]
            else:
                prediction = model_draw.predict(current_df)
            return prediction[0]
        else:
            return avoid_loss
        
    
    def avoid_loss(self, game_stat_ai):
        # find duplicates along rows
        rows = [[game_stat_ai[0], game_stat_ai[1], game_stat_ai[2]], [game_stat_ai[3], game_stat_ai[4], game_stat_ai[5]], [game_stat_ai[6], game_stat_ai[7], game_stat_ai[8]]]
        cols = [[game_stat_ai[0], game_stat_ai[3], game_stat_ai[6]], [game_stat_ai[1], game_stat_ai[4], game_stat_ai[7]], [game_stat_ai[2], game_stat_ai[5], game_stat_ai[8]]]
        diags = [[game_stat_ai[0], game_stat_ai[4], game_stat_ai[8]], [game_stat_ai[2], game_stat_ai[4], game_stat_ai[6]]]
        for row in rows:
            if self.find_first_duplicate_index(row) != None:
                return self.find_first_duplicate_index(row)
        # find duplicates along columns
        for col in range(3):
            if game_stat_ai[0][col] == game_stat_ai[1][col] == game_stat_ai[2][col] == 1 and game_stat_ai[0][col] == 0:
                return True


    def find_first_duplicate_index(arr):
        seen = set()
        for index, value in enumerate(arr):
            if value in seen:
                return index  # Return the index of the first duplicate
            seen.add(value)
        return None  # No duplicates found

    def print_body(self, game_status):
        # first pick the right element for the top row
        for top_row_element in range(len(game_status[0])):
            if top_row_element == 0:
                if game_status[0][top_row_element] == '':
                    top_row_left_element = self.upper_left_empty
                elif game_status[0][top_row_element] == 'x':
                    top_row_left_element = self.upper_left_x
                else:
                    top_row_left_element = self.upper_left_o
            if top_row_element == 1:
                if game_status[0][top_row_element] == '':
                    top_row_middle_element = self.upper_middle_empty
                elif game_status[0][top_row_element] == 'x':
                    top_row_middle_element = self.upper_middle_x
                else:
                    top_row_middle_element = self.upper_middle_o
            if top_row_element == 2:
                if game_status[0][top_row_element] == '':
                    top_row_right_element = self.upper_right_empty
                elif game_status[0][top_row_element] == 'x':
                    top_row_right_element = self.upper_right_x
                else:
                    top_row_right_element = self.upper_right_o
        # now pick the right element for the middle row
        for middle_row_element in range(len(game_status[1])):
            if middle_row_element == 0:
                if game_status[1][middle_row_element] == '':
                    middle_row_left_element = self.middle_left_empty
                elif game_status[1][middle_row_element] == 'x':
                    middle_row_left_element = self.middle_left_x
                else:
                    middle_row_left_element = self.middle_left_o
            if middle_row_element == 1:
                if game_status[1][middle_row_element] == '':
                    middle_row_middle_element = self.middle_middle_empty
                elif game_status[1][middle_row_element] == 'x':
                    middle_row_middle_element = self.middle_middle_x
                else:
                    middle_row_middle_element = self.middle_middle_o
            if middle_row_element == 2:
                if game_status[1][middle_row_element] == '':
                    middle_row_right_element = self.middle_right_empty
                elif game_status[1][middle_row_element] == 'x':
                    middle_row_right_element = self.middle_right_x
                else:
                    middle_row_right_element = self.middle_right_o
        # now pick the right element for the bottom row
        for lower_row_element in range(len(game_status[2])):
            if lower_row_element == 0:
                if game_status[2][lower_row_element] == '':
                    lower_row_left_element = self.lower_left_empty
                elif game_status[2][lower_row_element] == 'x':
                    lower_row_left_element = self.lower_left_x
                else:
                    lower_row_left_element = self.lower_left_o
            if lower_row_element == 1:
                if game_status[2][lower_row_element] == '':
                    lower_row_middle_element = self.lower_middle_empty
                elif game_status[2][lower_row_element] == 'x':
                    lower_row_middle_element = self.lower_middle_x
                else:
                    lower_row_middle_element = self.lower_middle_o
            if lower_row_element == 2:
                if game_status[2][lower_row_element] == '':
                    lower_row_right_element = self.lower_right_empty
                elif game_status[2][lower_row_element] == 'x':
                    lower_row_right_element = self.lower_right_x
                else:
                    lower_row_right_element = self.lower_right_o
        # now print the body
        for index in range(6):
            print(top_row_left_element[index] + top_row_middle_element[index] + top_row_right_element[index])
        for index in range(6):
            print(middle_row_left_element[index] + middle_row_middle_element[index] + middle_row_right_element[index])
        for index in range(5):
            print(lower_row_left_element[index] + lower_row_middle_element[index] + lower_row_right_element[index])

    def pick_player_to_start(self):
        current_player = np.random.choice(['x', 'o'])
        if current_player == 'x':
            print('\n' + "'X' STARTS THE ROUND!" + '\n')
        else:
            print('\n' + "'O' STARTS THE ROUND!" + '\n')
        return current_player
    
    def change_player(self, current_player):
        return 'o' if current_player == 'x' else 'x'
    
    def update_board(self, picked_field, current_player, board_status):
        print(current_player)
        row = (8 - (picked_field - 1)) // 3
        col = (picked_field - 1) % 3
        board_status[row][col] = current_player
        return board_status
    
    def player_input(self, board_status):
        while True:
            try:
                picked_field = input("Enter a number (1-9) corresponding to an empty field on the board: ")
                if picked_field.lower() == 'q':
                    return 'quit'
                picked_number = int(picked_field)
                # Validate if the input is within the acceptable range and the field is not already taken
                if 1 <= picked_number <= 9 and self.input_valid(picked_number, board_status):
                    return picked_number  # Valid input; exit the loop
                else:
                    print("Invalid input or field already taken. Please try again.")
            except ValueError:  # Specifically catch non-integer inputs
                print("Invalid input - only use numbers (1-9).")
    
    def check_for_winner(self, board_status):
        for row in board_status:
            if row.count('x') == 3:
                return 'x'
            elif row.count('o') == 3:
                return 'o'
        for col in range(3):
            if board_status[0][col] == board_status[1][col] == board_status[2][col] != '':
                return board_status[0][col]
        if board_status[0][0] == board_status[1][1] == board_status[2][2] != '':
            return board_status[0][0]
        elif board_status[0][2] == board_status[1][1] == board_status[2][0] != '':
            return board_status[0][2]
        return None
    
    def print_scoreboard(self, scoreboard):
        print(f"\nPlayer 'x' won {scoreboard['x']} times.")
        print(f"Player 'o' won {scoreboard['o']} times.\n")

    def check_for_draw(self, board_status):
        if all(cell != '' for row in board_status for cell in row):
            return True
        return False
