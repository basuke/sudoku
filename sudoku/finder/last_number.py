from ..solver.finder import Finder


class LastNumberFinder(Finder):
    """
    If some specific numbers are used for 8 times, the last one
    to be placed will be easily figured out.
    """
    def find(self, board):
        result = super(LastNumberFinder, self).find(board)

        for number in range(1, 10):
            cells = board.which_has(number)
            if len(cells) == (9 - 1):
                rows = board.rows.filter(lambda row: not number in row)
                cols = board.columns.filter(lambda col: not number in col)

                assert len(rows) == 1 and len(cols) == 1

                result.found(rows[0].crossing_cell(cols[0]), number)
                break

        return result
