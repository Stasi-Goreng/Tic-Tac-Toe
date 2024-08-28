from tic_tac_toe_body import game_functions
import os
import numpy as np
import time
import pandas as pd
from joblib import load

class TicTacToe:
    def __init__(self):
        self.game_body = game_functions()
        self.current_player = 'x' #decide on symbol to start with
        self.human_or_ai = np.random.choice([-1, 1])   #human=-1, ai=1
        self.board_status = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.picked_field = 0
        self.winner = False
        self.scoreboard = {
            "x": 0,
            "o": 0,
            "draws": 0
        }
        self.game_over = False
        self.game_record = []
        self.model_win_move_0 = load('ttt_model_x_wins_5_turns_only_move_0.joblib')
        self.model_win_move_1 = load('ttt_model_x_wins_5_turns_only_move_1.joblib')
        self.model_win_move_2 = load('ttt_model_x_wins_5_turns_only_move_2.joblib')
        self.model_win_move_3 = load('ttt_model_x_wins_5_turns_only_move_3.joblib')
        self.model_win_move_4 = load('ttt_model_x_wins_5_turns_only_move_4.joblib')
        self.model_win_move_5 = load('ttt_model_x_wins_5_turns_only_move_5_into_6.joblib')
        self.model_win_move_6 = load('ttt_model_x_wins_5_turns_only_move_6_into_7.joblib')
        self.model_win_move_7 = load('ttt_model_x_wins_5_turns_only_move_7_into_8.joblib')
        self.model_win_move_8 = load('ttt_model_x_wins_5_turns_only_move_8_into_9.joblib')
        #self.model_win_middle = load('ttt_model_x_wins_6to7_turns.joblib')
        self.model_draw = load('ttt_model_x_draws.joblib')
        self.num_turns = 0

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def ai_move(self):
        self.picked_field = self.game_body.ai_move(self.board_status, self.num_turns, self.model_win_move_0, self.model_win_move_1, self.model_win_move_2, self.model_win_move_3, self.model_win_move_4, self.model_win_move_5, self.model_win_move_6, self.model_win_move_7, self.model_win_move_8, self.model_draw)
        self.num_turns = self.num_turns + 1

    def player_input(self):
        self.picked_field = self.game_body.player_input(self.board_status)
        self.num_turns = self.num_turns + 1

    def print_board(self):
        self.game_body.print_body(self.board_status)
        self.print_scoreboard()

    def save_game(self):
        pd.DataFrame(self.game_record).to_csv('games.csv', index=False)

    def record_game(self):
        self.game_record.append(self.game_body.record_game(self.board_status))

    def update_board(self):
        self.board_status = self.game_body.update_board(self.picked_field, self.current_player, self.board_status)
        self.winner = self.game_body.check_for_winner(self.board_status)
        print(self.winner)
        self.human_or_ai *= -1 #swap player 
        # there is no winner yet
        if self.winner == None:
            self.check_for_draw()
            self.current_player = self.game_body.change_player(self.current_player)
        #there is a winner
        elif self.winner != None:
            self.clear_screen()
            self.print_board()
            #self.human_or_ai *= -1 #swap player after game ends
            print(f"{self.winner} won the game!")
            self.scoreboard[self.winner] += 1
            #self.print_scoreboard()
            time.sleep(3)
            self.reset_game()

    def print_scoreboard(self):
        self.game_body.print_scoreboard(self.scoreboard)

    def check_for_draw(self):
        if self.game_body.check_for_draw(self.board_status):
            self.clear_screen()
            self.print_board()
            self.scoreboard["draws"] += 1
            print("It's a draw!")
            self.print_scoreboard()
            time.sleep(3)
            self.human_or_ai *= -1 #swap player after game ends
            self.reset_game()

    def reset_game(self):
        self.board_status = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.current_player = self.game_body.change_player(self.current_player)
        self.winner = False
        self.num_turns = 0

    def play_game(self):
        while not self.game_over:
            self.print_board()
            if self.human_or_ai == -1:
                self.player_input()
            else:
                self.ai_move()
            if self.picked_field == 'quit':
                self.game_over = True
                break
            self.update_board() # update board, check for winner, update scoreboard and swap symbols
            self.clear_screen()

        print("\nFinal scoreboard:")
        self.print_scoreboard()
        print(f"saving game... (not really)")
        self.save_game()
        print("Game ended by user.")

