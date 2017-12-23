from ..solver.finder import Finder


class LastCellFinder(Finder):
    """
    if there is only one empty cell, the last number is apparent.

    ex: Row | 1 2 3 | 4 5 6 | X 8 9
    X = 7
    """
    def find(self, board):
        result = super(LastCellFinder, self).find(board)

        for region in board.rows + board.columns + board.boxes:
            cells = region.empty_cells
            if len(cells) == 1:
                numbers = region.available_numbers
                result.found(cells[0], numbers[0])
                break

        return result
