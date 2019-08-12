import Board
from Heuristics import *
from Agents import *

depth = 3



def gameLoop(board, white_agent, black_agent):
    while True:
        board.display()
        move = white_agent.chooseMove(board, 'w')
        if board.isInCheck('b'):
            print('Black is in check!')
            if board.checkmate('b'):
                print('Checkmate! White wins')
                break
        board.display()
        move = black_agent.chooseMove(board, 'b')
        if board.isInCheck('w'):
            print('White is in check!')
            if board.checkmate('w'):
                print('Checkmate! Black wins')
                break


if __name__ == '__main__':
    board = Board.Board()
    board.initialize()
    white_agent = None
    black_agent = None
    bad_choice = True
    choice_str = ''
    while bad_choice:
        print("""Choose player for white:
            1. Human
            2. MinimaxAgent""")
        choice_str = input()
        if choice_str.isdigit() and int(choice_str) > 0 and int(choice_str) < 3:
            bad_choice = False
    choice = int(choice_str)
    if choice == 1:
        white_agent = PlayerAgent('w')
    if choice == 2:
        white_agent = MinimaxAgent(depth, 'w')

    bad_choice = True
    choice_str = ''
    while bad_choice:
        print("""Choose player for black:
            1. Human
            2. MinimaxAgent""")
        choice_str = input()
        if choice_str.isdigit() and int(choice_str) > 0 and int(choice_str) < 3:
            bad_choice = False
    choice = int(choice_str)
    if choice == 1:
        black_agent = PlayerAgent('b')
    if choice == 2:
        black_agent = MinimaxAgent(depth, 'b')

    gameLoop(board, white_agent, black_agent)
