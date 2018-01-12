from sudoku.solver.solver import Solver
from sudoku.model.board import Board
from cmd import Cmd
from sudoku.presentation.printer import Printer
import re


class Console(Cmd):
    def preloop(self):
        self._start_game(Board("""
            . 4 . | 1 . . | . . .
            7 . . | . . 9 | . . 8
            . . 6 | . . . | 4 . .
            ------+-------+------
            . 7 . | . 1 . | . . .
            3 . . | 8 . 6 | . . 7
            . . . | . 5 . | . 9 .
            ------+-------+------
            . . 4 | . . . | 3 . .
            9 . . | 7 . . | . . 2
            . . . | . . 4 | . 6 .
        """))
        self.printer = Printer(self.stdout, None)

    def do_load(self, line):
        board = Board(line)
        self._start_game(board)
        print board

    def do_print(self, line=None):
        self.printer.out(self.solver.board)

    def do_set(self, line):
        pattern = re.compile(r"\s* \(? \s* (\d+) \s* , \s* (\d+) \s* \)? \s* = \s* (\d+) \s*", re.X )
        result = pattern.match(line)
        if result:
            x, y, num = result.groups()
            self.solver.board.cell(int(x), int(y)).set(int(num))

    def do_push(self, line):
        self.solver.save(comment=line)
        print "saved:", line

    def do_pop(self, line):
        comment = self.solver.restore()
        if comment is not None:
            print "restored:", comment
            self.do_print("")
        else:
            print "no board is saved"

    def do_stack(self, pattern):
        """Display saved board stack"""
        boards = self.solver.saved_boards()
        if not boards:
            print "no saved board"
            return
        else:
            print "%d boards saved" % len(boards)

        if pattern:
            boards = [(board, comment) for board, comment in boards if re.search(line, comment, re.IGNORECASE)]

        for index, (board, comment) in enumerate(boards):
            print "%d: %s" % (index + 1, comment)
            self.printer.out(board)

    def do_EOF(self):
        return True

    def emptyline(self):
        pass

    def _start_game(self, board):
        self.solver = Solver(board, [])

if __name__ == '__main__':
    Console().cmdloop()
