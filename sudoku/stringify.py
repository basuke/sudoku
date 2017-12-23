def stringify_cell(cell, detail=False):
    if not detail:
        return ('%s' % cell.number) if cell.number else '.'

    s = 'Cell(%s, %s' % (cell.x, cell.y)
    if cell.number:
        s += (', number=%d' % cell.number)
    return s + ')'


def stringify_list(a_list, detail=False):
    s = a_list.__class__.__name__ + '('
    if hasattr(a_list, 'identifier'):
        s += '#%s, ' % a_list.identifier

    if detail:
        s += str(list(a_list))
    else:
        s += "length=%d" % len(a_list)

    return s + ')'


def stringify_board(board, detail=False):
    lines = []

    if detail:
        lines += ["%d / %d filled" % (len(board.filled_cells), len(board))]
        lines += ["is_complete? %s" % board.is_complete]
        lines += ["is_finished? %s" % board.is_finished]
        lines += ["is_valid? %s" % board.is_valid]
        lines += [" / ".join("%d (%d)" % (num, len(board.which_has(num))) for num in range(1, 10))]

    for row in board.rows:
        line = ""

        for cell in row:
            if cell.x == 1:
                if cell.y > 1 and cell.y % 3 == 1:
                    lines.append('------+-------+------')
            else:
                line += ' '
                if cell.x % 3 == 1:
                    line += '| '

            line += str(cell)

        lines.append(line)

    return "\n".join(lines)

