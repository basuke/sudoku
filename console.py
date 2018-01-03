from sudoku.solver.solver import Solver
from cmd import Cmd


class Console(Cmd):
    def do_load(self, line):
        print "Hello", line

    def do_EOF(self):
        return True

    def preloop(self):
        pass

    def emptyline(self):
        pass

if __name__ == '__main__':
    Console().cmdloop()
