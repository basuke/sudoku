from .finder import FinderResult
from copy import copy


class Solver(object):
    def __init__(self, board, finders=None):
        self.board = board
        self.finders = finders or []
        self.steps = []
        self.boards = []

    @property
    def is_solving(self):
        return not self.board.is_finished and self.board.is_valid

    def step(self, verbose=False):
        self.board.constraints.clear()

        for finder in self.finders:
            finder.prepare(self.board)

            result = finder.find(self.board)
            if result:
                result.cell.set(result.number)
                if verbose:
                    print self.board
                    print " >", result
                return result

        if verbose:
            print self.board

        return None

    def solve(self, verbose=False):
        while self.is_solving:
            found = self.step(verbose)
            if not found:
                return False

            self.steps.append(found)

        return self.board.is_finished

    def save(self, comment=""):
        self.boards.append((copy(self.board), comment))

    def restore(self):
        if self.boards:
            self.board, comment = self.boards.pop()
            return comment
        else:
            return None

    def saved_boards(self):
        return self.boards