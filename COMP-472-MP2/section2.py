from skeleton import Game
import string

class Game_Parameter:
#Variable setup
    size_of_board = num_of_blocs = position_of_blocs = line_up_size = max_depth_d1 = max_depth_d2 = threshold = 0
    blocs_x_coord = blocs_y_coord = 0
    blocs_coordinates = []
    minimax_alphabeta_bool = False #default minimax (False) - Alphabeta (True)
    play_modes = ""
    board = []

    def __init__(self):
        print ("Welcome to the Game of Line 'em Up")

        self.size_of_board = input("\nPlease Enter the size of the board between 3-10:\n")
        self.size_of_board = int(self.size_of_board)

        while (self.size_of_board < 3) or (self.size_of_board > 10):
            print("Invalid input")
            self.size_of_board = input("Please Enter the size of the board between 3-10:\n")
            self.size_of_board = int(self.size_of_board)

        num_of_blocs = input("\nPlease Enter the number of blocs between 0-" + str(2*self.size_of_board) + ":\n")
        num_of_blocs = int(num_of_blocs)

        while (num_of_blocs < 0) or (num_of_blocs > (2*self.size_of_board)):
            print("Invalid input")
            num_of_blocs = input("\nPlease Enter the number of blocs between 0-" + str(2*self.size_of_board) + ":\n")
            num_of_blocs = int(num_of_blocs)

        print(num_of_blocs)

        for i in range(num_of_blocs):
            blocs_x_coord = input("Please enter the x coordinate of the bloc " + str(i+1) + "\n")
            blocs_x_coord = int(blocs_x_coord)
            while blocs_x_coord < 0 or blocs_x_coord > self.size_of_board:
                print("Invalid input")
                blocs_x_coord = input("Please enter the x coordinate of the bloc " + str(i+1) + "\n")
                blocs_x_coord = int(blocs_x_coord)

            #Take in Y coordinates
            blocs_y_coord = input("Please enter the y coordinate of the bloc " + str(i+1) + "\n")
            blocs_y_coord = int(blocs_y_coord)
            while blocs_y_coord < 0 or blocs_y_coord > self.size_of_board:
                print("Invalid input")
                blocs_y_coord = input("Please enter the y coordinate of the bloc " + str(i+1) + "\n")
                blocs_y_coord = int(blocs_y_coord)

            self.blocs_coordinates.append((blocs_x_coord, blocs_y_coord))

        print (self.blocs_coordinates)

        line_up_size = input("\nPlease enter the winning line-up size 3-" + str(self.size_of_board) + ":\n")
        line_up_size = int(line_up_size)

        while (line_up_size < 3) or (line_up_size > self.size_of_board):
            print("Invalid input")
            line_up_size = input("Please enter the winning line-up size 3-" + str(self.size_of_board) + ":\n")
            line_up_size = int(line_up_size)

        print(line_up_size)

        threshold = input("\nPlease enter the maximum allowed time (in seconds) for the program to return a move:\n")
        threshold = int(threshold)

        search_algo = input("\nPlease enter the desired search algorithm (minimax OR alphabeta):\n")
        while (search_algo.lower() != "minimax") and (search_algo.lower() != "alphabeta"):
            print("Invalid input")
            search_algo = input("\nPlease enter the desired search algorithm (minimax OR alphabeta):\n")

        if search_algo == 'minimax':
            minimax_alphabeta_bool = False
        else:
            minimax_alphabeta_bool = True

        print (minimax_alphabeta_bool)

        self.play_modes = input("Please enter the play modes (i.e. H-H, H-AI, AI-H, AI-AI):\n")
        while (self.play_modes.lower() != "h-h") and (self.play_modes.lower() != "h-ai") and (self.play_modes.lower() != "ai-h") and (self.play_modes.lower() != "ai-ai"):
            print("Invalid input")
            self.play_modes = input("Please enter the play modes (i.e. H-H, H-AI, AI-H, AI-AI):\n")

        print(self.play_modes)

    # Attempting to pring the board
    def init_board(self):
        for i in range(self.size_of_board):
            row = []
            for j in range(self.size_of_board):
                row.append('.')
            self.board.append(row)
        for k, z, in enumerate(self.blocs_coordinates):
            x = z[0]
            y = z[1]
            self.board[x][y] = '*'

    def display_board(self):
        formatted_list = ' '
        for i in range(self.size_of_board):
            formatted_list += ' ' + string.ascii_uppercase[i]
        row_index = 0
        for i in self.board:
            formatted_list += '\n' + str(row_index) + '|'
            col_index = 0
            row_index += 1
            for j in i:
                formatted_list += j + ' '
                col_index += 1
        print(formatted_list)

    def coords_of_moves(self):
        column_selected = ''
        row_selected = ''

        if 'h' in self.play_modes:
            column_selected = input("Please indicate the column [A-" + string.ascii_uppercase[self.size_of_board -1] + "]:\n")
            while column_selected not in [string.ascii_uppercase[i] for i in range(self.size_of_board)]:
                print("Invalid input")
                column_selected = input("Please indicate the column [A-" + string.ascii_uppercase[self.size_of_board - 1] + "]:\n")

            row_selected = int(input("Please indicate the row [0-" + str(self.size_of_board -1) + "]:\n"))
            while row_selected not in [i for i in range(self.size_of_board)]:
                print("Invalid input")
                row_selected = int(input("Please indicate the row [0-" + str(self.size_of_board -1) + "]:\n"))
            
            return column_selected + str(row_selected)




            

# Coordinates of Moves: If at least one player is a human, then their moves will be specified by first
# indicating the column (numbered [A..J]), then the row (numbered [0..(n-1)]), for example B 3. Note
# that if a human player enters an illegal move (e.g. W 3 or the coordinates of a position that is not empty),
# then they will only be warned and be given a chance to enter another move with no penalty3
# . However, if
# your program generates an illegal move, then it will automatically lose the game.

