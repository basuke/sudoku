from sudoku.solver.solver import Solver
from cmd import Cmd

class Console(Cmd):
    def do_load(self, line):
        print "Hello", line


if __name__ == '__main__':
    Console().cmdloop()
