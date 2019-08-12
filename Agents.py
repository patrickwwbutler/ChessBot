from Board import *
from Heuristics import *

class Agent(object):
    def __init__(self):
        self.heuristic = heuristic

    def chooseMove(self, board, side):
        raise NotImplementedError

    def setHeuristic(self):
        raise NotImplementedError


class PlayerAgent(Agent):
    def __init__(self, side):
        self.side = side
        self.letters = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

    def chooseMove(self, board, side):
        goodmove = False
        move = None
        while not goodmove:
            move = self.handleInput()
            if move != None:
                goodmove = board.isLegalMove(move, self.side)
                if not goodmove:
                    print("Error: invalid move")
        board.enterMove(move)

    def handleInput(self):
        command = input()
        coords = command.split(' ')
        if len(coords) != 2:
            print('Error: invalid command')
            return None
        startcol = coords[0][0]
        if not startcol.isalpha():
            print('Error: invalid command')
            return None
        col1 = self.letters[startcol.upper()]
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
        col2 = self.letters[endcol.upper()]
        endrow = coords[1][1]
        if not endrow.isdigit():
            print('Error: invalid command')
            return None
        row2 = int(endrow)
        row2 = 8 - row2
        end = (row2, col2)
        return (start, end)


class MinimaxAgent(Agent):
    def __init__(self, depth, side):
        self.heuristic = NaiveHeuristic()
        self.depth = depth
        self.side = side

    def chooseMove(self, board, side):
        moves = board.getMovesForSide(side)
        best_score = -float('inf')
        best_move = None
        for move in moves:
            score = self.evalMin(board.generateSuccessor(move), otherSide(side), 1)
            if score > best_score:
                best_score = score
                best_move = move
        board.enterMoveAuto(best_move)


    def evalMin(self, board, side, depth):
        if depth == self.depth:
            return self.heuristic.evaluate(board, self.side)
        moves = board.getMovesForSide(side)
        return min([self.evalMax(board.generateSuccessor(move), otherSide(side), depth + 1) for move in moves])

    def evalMax(self, board, side, depth):
        if depth == self.depth:
            return self.heuristic.evaluate(board, self.side)
        moves = board.getMovesForSide(side)
        return max([self.evalMin(board.generateSuccessor(move), otherSide(side), depth + 1) for move in moves])


# class AlphaBetaPruningAgent(Agent):
#     def __init__(self, depth, side):
#         self.heuristic = NaiveHeuristic()
#         self.depth = depth
#         self.side = side
#
#     def chooseMove(self, board):
#         moves = board.getMovesForSide(self.side)
#         alpha
