from Board import *

class Heuristic(object):
    def evaluate(self, board): raise NotImplementedError


class NaiveHeuristic(Heuristic):
    def evaluate(self, board, side):
        friendlies = board.getPiecesFromSide(side)
        score = 0
        for piece in friendlies:
            score += piece.value
        enemies = board.getPiecesFromSide(otherSide(side))
        for piece in enemies:
            score -= piece.value
        return score
