from ..solver.finder import Finder


class LastOneFinder(Finder):
    def find(self, board):
        result = super(LastOneFinder, self).find(board)

        for region in board.rows + board.columns + board.areas:
            cells = region.empty_cells
            if len(cells) == 1:
                numbers = region.available_numbers
                result.found(cells[0], numbers[0])
                break

        return result
