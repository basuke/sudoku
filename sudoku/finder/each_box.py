from ..solver.finder import Finder


class EachBoxFinder(Finder):
    def find(self, board):
        result = super(EachBoxFinder, self).find(board)

        for number in range(1, 10):
            for box in board.boxes.filter(lambda box: number not in box):
                cells = box.empty_cells.filter(lambda cell: cell.can_be(number))
                if len(cells) == 1:
                    result.found(cells._1st, number)
                    break

        return result