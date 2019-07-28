from Board import Board


letters = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

def handleInput():
    command = input()
    coords = command.split(' ')
    if len(coords) != 2:
        print('Error: invalid command')
        return None
    startrow = coords[0][0]
    if not startrow.isalpha():
        print('Error: invalid command')
        return None
    row1 = letters[startrow]
    startcol = coords[0][1]
    if not startcol.isdigit():
        print('Error: invalid command')
        return None
    col1 = int(startcol)
    col1 -= 1
    start = (row1, col1)
    endrow = coords[1][0]
    if not endrow.isalpha():
        print('Error: invalid command')
        return None
    row2 = letters[endrow]
    endcol = coords[1][1]
    if not endcol.isdigit():
        print('Error: invalid command')
        return None
    col2 = int(endcol)
    col2 -= 1
    end = (row2, col2)
    return (start, end)


if __name__ == '__main__':
    board = Board()
    board.initialize()
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
        board.display()
        goodmove = False
        move = None
        while not goodmove:
            move = handleInput()
            if move != None:
                goodmove = board.isLegalMove(move, 'b')
        board.enterMove(move)
