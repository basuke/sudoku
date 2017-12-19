def parse(numbers):
    for c in numbers:
        if c == '.':
            yield None
        elif c >= '0' and c <= '9':
            yield ord(c) - 0x30

def parse2d(number_str):
    """read sudoku replesentation and parse it to 81 numbers"""
    rows = []
    cols = []

    for number in number_str:
        if number == '\n':
            cols = []
        elif number == '.' or (number >= '0' and number <= '9'):
            if number == '.':
                number = None
            else:
                number = ord(number) - 0x30

            if not cols:
                rows.append(cols)

            cols.append(number)

    return rows

