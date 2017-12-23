class Finder(object):
    def __init__(self):
        pass

    def prepare(self, board):
        pass

    def find(self, board):
        return FinderResult(self)


class FinderResult(object):
    def __init__(self, finder):
        self.finder = finder
        self.cell = None
        self.number = None

    def __nonzero__(self):
        return self.cell is not None and self.number

    def found(self, cell, number):
        self.cell = cell
        self.number = number

    def do_it(self):
        self.cell.set(self.number)

    def __str__(self):
        return "%s => (%d, %d) : %s" % (self.number, self.cell.x, self.cell.y, self.finder)
