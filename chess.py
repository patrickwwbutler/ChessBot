from Board import Board
from heuristics import *

# TO DO
# Check that no pieces are in the way of multiple square moves for rook, bishop, queen
# Ensure checkmate works properly


letters = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

def handleInput():
    command = input()
    coords = command.split(' ')
    if len(coords) != 2:
        print('Error: invalid command')
        return None
    startcol = coords[0][0]
    if not startcol.isalpha():
        print('Error: invalid command')
        return None
    col1 = letters[startcol.upper()]
    startrow = coords[0][1]
    if not startrow.isdigit():
        print('Error: invalid command')
        return None
    row1 = int(startrow)
    row1 = 8 - row1
    start = (row1, col1)
    endcol = coords[1][0]
    if not endcol.isalpha():
        print('Error: invalid command')
        return None
    col2 = letters[endcol.upper()]
    endrow = coords[1][1]
    if not endrow.isdigit():
        print('Error: invalid command')
        return None
    row2 = int(endrow)
    row2 = 8 - row2
    end = (row2, col2)
    return (start, end)


if __name__ == '__main__':
    board = Board()
    board.initialize()
    heuristic = NaiveHeuristic()
    while True:
        board.display()
        goodmove = False
        move = None
        while not goodmove:
            move = handleInput()
            if move != None:
                goodmove = board.isLegalMove(move, 'w')
                if not goodmove:
                    print("Error: invalid move")
        board.enterMove(move)
        if board.isInCheck('b'):
            print('Black is in check!')
            if board.checkmate('b'):
                print('Checkmate! White wins')
                break
        board.display()
        print('Score: ', heuristic.evaluate(board, 'w'))
        goodmove = False
        move = None
        while not goodmove:
            move = handleInput()
            if move != None:
                goodmove = board.isLegalMove(move, 'b')
        board.enterMove(move)
        if board.isInCheck('w'):
            print('White is in check!')
            if board.checkmate('w'):
                print('Checkmate! Black wins')
                break
