from section2 import game_parameter, print_board, size_of_board
from skeleton import Game

def main():
    g = Game(recommend=True)
    g.play(algo=Game.ALPHABETA,player_x=Game.AI,player_o=Game.AI)
    g.play(algo=Game.MINIMAX,player_x=Game.AI,player_o=Game.HUMAN)
    #game_parameter()
    #print_board(4)

if __name__ == "__main__":
	main()