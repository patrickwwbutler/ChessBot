from Pieces import *

def inBounds(x):
    return x >= 0 and x < 8

class Board(object):
    def __init__(self):
        row = [None]*8
        self.board = []
        self.pieces = {}
        self.pieces['w'] = []
        self.pieces['b'] = []
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
            print("Move not inbounds")
            return False
        if start == None:
            print("No piece at start square")
            return False
        if start.side != side:
            print("Piece at starting square is not yours")
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
                    if diag1 != None and diag1.side != start.side:
                        legalmoves.append((coeff, 1))
                if start.c - 1 >= 0:
                    diag2 = self.board[start.r+coeff][start.c-1]
                    if diag2 != None and diag2.side != start.side:
                        legalmoves.append((coeff, -1))

            if start.hasMoved == False:
                legalmoves.append((2*coeff, 0))
        netmove = ((move[1][0] - move[0][0]), (move[1][1] - move[0][1]))
        return netmove in legalmoves


    def enterMove(self, move):
        piece = self.board[move[0][0]][move[0][1]]
        self.board[move[1][0]][move[1][1]] = piece
        piece.r = move[1][0]
        piece.c = move[1][1]
        self.board[move[0][0]][move[0][1]] = None

        if piece.type == 'P':
            piece.hasMoved = True
            if (move[1][1] == 0 and piece.side == 'w') or (move[1][1] == 7 and piece.side == 'b'):
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

        def isInCheck()
