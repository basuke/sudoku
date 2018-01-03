from ..solver.finder import Finder


class OneChoiceFinder(Finder):
    def find(self, board):
        result = super(OneChoiceFinder, self).find(board)

        for region in board.boxes + board.rows + board.columns:
            for number in range(1, 10):
                cells = region.possible_cells_with(number)
                if len(cells) == 1:
                    result.found(cells.pop(), number)
                    return result

        return result
