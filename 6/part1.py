def read_data():
    with open('input.txt', 'r') as f:
        data = f.read()

    return [list(x) for x in data.split('\n') if len(x) > 0]


cursors = ['^', 'v', '<', '>']


def get_cursor(data):
    for row, l in enumerate(data):
        for col, c in enumerate(l):
            if c in cursors:
                return row, col, c
    raise Exception('cursor not found!')


def step(data):
    row, col, c = get_cursor(data)

    data[row][col] = 'X'
    next_row = row
    next_col = col

    if c == '^':
        next_row = row - 1
        nc = '>'
    elif c == 'v':
        next_row = row + 1
        nc = '<'
    elif c == '>':
        next_col = col + 1
        nc = 'v'
    elif c == '<':
        next_col = col - 1
        nc = '^'
    else:
        raise Exception('unknown command')

    if next_row < 0 or next_row >= len(data):
        return False

    if next_col < 0 or next_col >= len(data[next_row]):
        return False

    s = data[next_row][next_col]
    if s == '#':
        data[row][col] = nc
    else:
        data[next_row][next_col] = c

    return True


def cc(data):
    return sum([len([x for x in line if x == 'X']) for line in data])


data = read_data()
while step(data):
    continue

out = cc(data)
print(out)
