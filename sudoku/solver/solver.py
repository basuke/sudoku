from .finder import FinderResult


class Solver(object):
    def __init__(self, board, finders=None):
        self.board = board
        self.finders = finders or []
        self.steps = []

    @property
    def is_solving(self):
        return not self.board.is_finished and self.board.is_valid

    def step(self):
        for finder in self.finders:
            finder.prepare(self.board)

            result = finder.find(self.board)
            if result:
                result.cell.set(result.number)
                return result

        return None

    def solve(self):
        while self.is_solving:
            found = self.step()
            if not found:
                return False

            self.steps.append(found)

        return self.board.is_finished