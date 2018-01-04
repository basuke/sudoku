from sudoku.model.board import Board


class Printer(object):
    def __init__(self, stdout, stderr):
        self.stdout = stdout
        self.stderr = stderr

    def out(self, obj):
        if issubclass(Board, obj.__class__):
            lines = self.dump_board(obj)
        else:
            raise RuntimeError("Unknown type")

        for line in lines:
            self.stdout.write(line + "\n")

    def dump_board(self, board):
        def dump_row(row):
            line = "%s%d%s | " % ("", row.y, "")
            for cell in row:
                line += "%s%s%s " % (("", str(cell.number), "") if cell else ("", ".", ""))
                if cell.x % 3 == 0:
                    line += "| "
            return line

        lines = [dump_row(row) for row in board.rows]

        lines.append("  +-------+-------+-------+ ")
        lines.insert(6, "  +-------+-------+-------+ ")
        lines.insert(3, "  +-------+-------+-------+ ")
        lines.insert(0, "  +-------+-------+-------+ ")
        lines.insert(0, "    1 2 3   4 5 6   7 8 9   ")

        return lines
