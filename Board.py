from Pieces import *
from copy import deepcopy

def inBounds(x):
    return x >= 0 and x < 8

def otherSide(side):
    if side == 'w':
        return 'b'
    else:
        return 'w'

def getCoeff(side):
    if side == 'w':
        return -1
    else:
        return 1


class Board(object):
    def __init__(self):
        row = [None]*8
        self.board = []
        self.pieces = {}
        self.pieces['w'] = []
        self.pieces['b'] = []
        self.inCheck = {}
        self.inCheck['w'] = False
        self.inCheck['b'] = False
        for i in range(0, 8):
            self.board.append(list(row))


    def checkPos(self, r, c):
        return self.board[r][c]


    def display(self):
        print('   ---------------------------------')
        i = 0
        for row in self.board:
            print(8 - i, end="  ")
            i += 1
            print('| ', end='')
            for piece in row:
                if piece != None:
                    print(piece.display(), end=' | ')
                else:
                    print(' ', end=' | ')
            print('')
            print('   ---------------------------------')
        print('     A   B   C   D   E   F   G   H')
        print()

    def placeAt(self, piece, r, c):
        self.board[r][c] = piece


    def initialize(self):
        for i in range(0, 8):
            p1 = Pawn(1, i, 'b')
            self.pieces['b'].append(p1)
            self.board[1][i] = p1
            p2 = Pawn(6, i, 'w')
            self.pieces['w'].append(p2)
            self.board[6][i] = p2
        for i in range(0, 2):
            r = i*7
            if r == 0:
                s = 'b'
            else:
                s = 'w'
            r1 = Rook(r, 0, s)
            self.pieces[s].append(r1)
            self.board[r][0] = r1

            kn1 = Knight(r, 1, s)
            self.pieces[s].append(kn1)
            self.board[r][1] = kn1

            b1 = Bishop(r, 2, s)
            self.pieces[s].append(b1)
            self.board[r][2] = b1

            q1 = Queen(r, 3, s)
            self.pieces[s].append(q1)
            self.board[r][3] = q1

            k1 = King(r, 4, s)
            self.pieces[s].append(k1)
            self.board[r][4] = k1

            r2 = Rook(r, 7, s)
            self.pieces[s].append(r2)
            self.board[r][7] = r2

            kn2 = Knight(r, 6, s)
            self.pieces[s].append(kn2)
            self.board[r][6] = kn2

            b2 = Bishop(r, 5, s)
            self.pieces[s].append(b2)
            self.board[r][5] = b2


    def isLegalMove(self, move, side):
        start = self.board[move[0][0]][move[0][1]]
        if not inBounds(move[1][0]) or not inBounds(move[1][1]):
            return False
        if start == None:
            return False
        if start.side != side:
            return False
        netmove = ((move[1][0] - move[0][0]), (move[1][1] - move[0][1]))
        end = self.board[move[1][0]][move[1][1]]
        if end != None and end.side == side:
            return False
        legalmoves = list(start.getMoves())
        if start.type == 'P':
            coeff = 0
            if start.side == 'w':
                coeff = -1
            else:
                coeff = 1
            if start.r + coeff < 8 and start.r + coeff >= 0:
                if start.c + 1 < 8:
                    diag1 = self.board[start.r+coeff][start.c+1]
                    if diag1 == None or diag1.side == start.side:
                        legalmoves.remove((coeff, 1))
                if start.c - 1 >= 0:
                    diag2 = self.board[start.r+coeff][start.c-1]
                    if diag2 == None or diag2.side == start.side:
                        legalmoves.remove((coeff, -1))
            if self.board[move[1][0]][move[1][1]] != None and move[1][1] - move[0][1] == 0:
                return False

            if start.hasMoved == False and self.board[move[0][0]+coeff][move[0][1]] == None:
                legalmoves.append((2*coeff, 0))
        if netmove not in legalmoves:
            return False

        if start.type == 'R' or start.type == 'B' or start.type == 'Q':
            row_diff = move[1][0] - move[0][0]
            col_diff = move[1][1] - move[0][1]
            row_coeff = 0
            if row_diff > 0:
                row_coeff = 1
            elif row_diff < 0:
                row_coeff = -1
            col_coeff = 0
            if col_diff > 0:
                col_coeff = 1
            elif col_diff < 0:
                col_coeff = -1
            for i in range(1, max(abs(row_diff), abs(col_diff))):
                if self.board[move[0][0]+i*row_coeff][move[0][1]+i*col_coeff] != None:
                    return False


        validmove = netmove in legalmoves
        if not validmove:
            return False
        if self.inCheck[side]:
            if self.generateSuccessor(move).isInCheck(side):
                return False
        return netmove in legalmoves


    def enterMove(self, move):
        piece = self.board[move[0][0]][move[0][1]]
        target = self.board[move[1][0]][move[1][1]]
        if target != None:
            start_side = piece.side
            self.pieces[otherSide(start_side)].remove(target)
        self.board[move[1][0]][move[1][1]] = piece
        piece.r = move[1][0]
        piece.c = move[1][1]
        self.board[move[0][0]][move[0][1]] = None

        if piece.type == 'P':
            piece.hasMoved = True
            if (move[1][0] == 0 and piece.side == 'w') or (move[1][0] == 7 and piece.side == 'b'):
                print("""Choose a piece to promote your pawn to:
                    1. Knight
                    2. Bishop
                    3. Rook
                    4. Queen""")
                bad_input = True
                selection_int = -1
                while bad_input:
                    selection = input()
                    if selection.isdigit():
                        selection_int = int(selection)
                        if selection_int >= 1 and selection_int <= 4:
                            bad_input = False
                if selection_int == 1:
                    self.board[move[1][0]][move[1][1]] = Knight(piece.r, piece.c, piece.side)
                if selection_int == 2:
                    self.board[move[1][0]][move[1][1]] = Bishop(piece.r, piece.c, piece.side)
                if selection_int == 3:
                    self.board[move[1][0]][move[1][1]] = Rook(piece.r, piece.c, piece.side)
                if selection_int == 4:
                    self.board[move[1][0]][move[1][1]] = Queen(piece.r, piece.c, piece.side)


    def isInCheck(self, side):
        king = None
        for piece in self.pieces[side]:
            if piece.type == 'K':
                king = piece
        king_coords = (king.r, king.c)

        for piece in self.pieces[otherSide(side)]:
            piece_coords = (piece.r, piece.c)
            if self.isLegalMove((piece_coords, king_coords), piece.side):
                return True
        return False


    def checkmate(self, side):
        # if this is called, we can assume the king is at least in check
        for piece in self.pieces[side]:
            moves = list(piece.moves)
            if piece.type == 'P' and not piece.hasMoved:
                moves.append((getCoeff(side)*2, 0))
            for move in moves:
                move_alt = ((piece.r, piece.c), (piece.r + move[0], piece.c + move[1]))
                if self.isLegalMove(move_alt, side):
                    if not self.generateSuccessor(move_alt).isInCheck(side):
                        print('move ', move_alt, ' can escape check')
                        return False
        return True


    def generateSuccessor(self, move):
        new_board = deepcopy(self)
        new_board.enterMove(move)
        return new_board

    def getPiecesFromSide(self, side):
        return self.pieces[side]
