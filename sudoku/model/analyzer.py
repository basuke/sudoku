class Analyzer(object):
    def __init__(self, *args):
        self._args = args

    def analyze(self, board):
        raise RuntimeError("not implemented")

    def will_bind(self, board):
        pass

    def did_bind(self, board):
        pass

    def __eq__(self, other):
        """
        :type other: Analyzer
        """
        return self.__class__ == other.__class__ and self._args == other._args

