from Board import *

class Heuristic(object):
    def evaluate(self, board): raise NotImplementedError


class NaiveHeuristic(Heuristic):
    def __init__(self):
        print('Using naive heuristic')

    def evaluate(self, board, side):
        score = 0
        if board.isInCheck(otherSide(side)):
            score += 10
            if board.checkmate(otherSide(side)):
                score += 1000
        friendlies = board.getPiecesFromSide(side)
        for piece in friendlies:
            score += piece.value
        enemies = board.getPiecesFromSide(otherSide(side))
        for piece in enemies:
            score -= piece.value
        return score
