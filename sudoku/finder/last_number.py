from ..solver.finder import Finder


class LastNumberFinder(Finder):
    def find(self, board):
        result = super(LastNumberFinder, self).find(board)

        for number in range(1, 10):
            cells = board.which_has(number)
            if len(cells) == (9 - 1):
                numbers = set(range(1, 10))
                x = (numbers - set(cell.x for cell in cells)).pop()
                y = (numbers - set(cell.y for cell in cells)).pop()

                result.found(board.cell(x, y), number)
                break

        return result
