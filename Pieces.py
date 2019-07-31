class Piece(object):
    def __init__(self):
        self.moves = []
        self.value = 0
        self.type = "none"
        self.r = -1
        self.c = -1
        self.side = ''
    def getMoves(self):
        return list(self.moves)
    def getValue(self):
        return self.value
    def getType(self):
        return self.type
    def display(self):
        if self.side == 'b':
            return self.type.lower()
        else:
            return self.type



class Pawn(Piece):
    def __init__(self, r, c, side):
        self.r = r
        self.c = c
        self.side = side
        if self.side == 'b':
            coeff = 1
        else:
            coeff = -1
        self.moves = [(coeff, 0), (coeff, 1), (coeff, -1)]
        self.value = 1
        self.type = 'P'
        self.hasMoved = False

class Rook(Piece):
    def __init__(self, r, c, side):
        self.r = r
        self.c = c
        self.side = side
        self.type = 'R'
        self.moves = [(0, i) for i in range(-7, 8)] + [(i, 0) for i in range(-7, 8)]
        self.moves.remove((0, 0))
        self.value = 5

class Knight(Piece):
    def __init__(self, r, c, side):
        self.r = r
        self.c = c
        self.side = side
        self.value = 3
        self.moves = [(1, 2), (2, 1), (-1, 2), (-1, -2), (-2, 1), (-2, -1), (1, -2), (2, -1)]
        self.type = 'H'

class Bishop(Piece):
    def __init__(self, r, c, side):
        self.r = r
        self.c = c
        self.side = side
        self.value = 3
        self.moves = [(i, i) for i in range(-7, 8)] + [(i, -i) for i in range(-7, 8)]
        self.moves.remove((0, 0))
        self.type = 'B'

class Queen(Piece):
    def __init__(self, r, c, side):
        self.r = r
        self.c = c
        self.side = side
        self.value = 9
        self.moves = [(i, i) for i in range(-7, 8)] + [(i, -i) for i in range(-7, 8)] + [(0, i) for i in range(-7, 8)] + [(i, 0) for i in range(-7, 8)]
        self.moves.remove((0, 0))
        self.type = 'Q'

class King(Piece):
    def __init__(self, r, c, side):
        self.r = r
        self.c = c
        self.side = side
        self.value = float('inf')
        self.moves = [(0, 1), (1, 1), (-1, 1), (1, 0), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        self.type = 'K'
