from sudoku.solver.solver import Solver
from sudoku.model.board import Board
from cmd import Cmd
from sudoku.presentation.printer import Printer
import re


class Console(Cmd):
    def preloop(self):
        self._start_game(Board("123...456improt"))
        self.printer = Printer(self.stdout, None)

    def do_load(self, line):
        board = Board(line)
        self._start_game(board)
        print board

    def do_print(self, line):
        self.printer.out(self.solver.board)

    def do_set(self, line):
        pattern = re.compile(r"\s* \(? \s* (\d+) \s* , \s* (\d+) \s* \)? \s* = \s* (\d+) \s*", re.X )
        result = pattern.match(line)
        if result:
            x, y, num = result.groups()
            self.solver.board.cell(int(x), int(y)).set(int(num))

    def do_EOF(self):
        return True

    def emptyline(self):
        pass

    def _start_game(self, board):
        self.solver = Solver(board, [])

if __name__ == '__main__':
    Console().cmdloop()
