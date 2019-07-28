from Pieces import *

class Board(object):
    def __init__(self):
        row = [None]*8
        self.board = []
        for i in range(0, 8):
            self.board.append(list(row))


    def checkPos(self, r, c):
        return self.board[r][c]

    def display(self):
        print('  ---------------------------------')
        i = 0
        rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for row in self.board:
            print(rows[i], end="  ")
            i += 1
            print('| ', end='')
            for piece in row:
                if piece != None:
                    print(piece.display(), end=' | ')
                else:
                    print(' ', end=' | ')
            print('')
            print('  ---------------------------------')
        print('    1   2   3   4   5   6   7   8')
        print()

    def placeAt(self, piece, r, c):
        self.board[r][c] = piece

    def initialize(self):
        for i in range(0, 8):
            p1 = Pawn(1, i, 'b')
            self.board[1][i] = p1
            p2 = Pawn(6, i, 'w')
            self.board[6][i] = p2
        for i in range(0, 2):
            r = i*7
            if r == 0:
                s = 'b'
            else:
                s = 'w'
            r1 = Rook(r, 0, s)
            self.board[r][0] = r1
            kn1 = Knight(r, 1, s)
            self.board[r][1] = kn1
            b1 = Bishop(r, 2, s)
            self.board[r][2] = b1
            q1 = Queen(r, 3, s)
            self.board[r][3] = q1
            k1 = King(r, 4, s)
            self.board[r][4] = k1
            r2 = Rook(r, 7, s)
            self.board[r][7] = r2
            kn2 = Knight(r, 6, s)
            self.board[r][6] = kn2
            b2 = Bishop(r, 5, s)
            self.board[r][5] = b2

    def isLegalMove(self, move, side):
        start = self.board[move[0][0]][move[0][1]]
        if start == None:
            return False
        if start.side != side:
            return False
        legalmoves = list(start.getMoves())
        if start.type == 'P':
            coeff = 0
            if start.side == 'w':
                coeff = -1
            else:
                coeff = 1
            diag1 = self.board[move[0][0]+coeff][move[0][1]+1]
            if diag1 != None and diag1.type != start.type:
                legalmoves.append((coeff, 1))
            diag2 = self.board[move[0][0]+coeff][move[0][1]-1]
            if diag2 != None and diag2.type != start.type:
                legalmoves.append((coeff, -1))

            if start.hasMoved == False:
                legalmoves.append((2*coeff, 0))
        netmove = ((move[1][0] - move[0][0]), (move[1][1] - move[0][1]))
        return netmove in legalmoves

    def enterMove(self, move):
        piece = self.board[move[0][0]][move[0][1]]
        self.board[move[1][0]][move[1][1]] = piece
        self.board[move[0][0]][move[0][1]] = None
