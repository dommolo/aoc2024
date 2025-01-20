import sys

class LoopException(Exception):
    pass

class TerminationException(Exception):
    pass


def read_data():
    with open('input.txt', 'r') as f:
        data = f.read()

    return [list(x) for x in data.split('\n') if len(x) > 0]


cursors = ['v', '<', '^', '>']
obstacles = ['#', 'O', 'N', 'S', 'W', 'E']

# from N = 1000 = 8
# from E = 0100 = 4
# from S = 0010 = 2
# from W = 0001 = 1

def check_obstacle(o, c):
    if o in ['#', 'O']:
        return False
    
    b = '{0:04b}'.format(int(o))
    v = b[cursors.index(c)]
    return v == '1'


def update_obstacle(o, c):
    if o in ['#', 'O']:
        b = '0000'
    else:
        b = '{0:04b}'.format(int(o))
        
    i = cursors.index(c)
    ub = b[:i] + '1' + b[i+1:]
    #print(f'update cursor: {o} {c} {i} {b} -> {ub}')
    return str(int(ub, 2))


def get_start(data):
    for row, l in enumerate(data):
        for col, c in enumerate(l):
            if c in cursors:
                return row, col, c
    raise Exception('start not found!')


def get_trail(c):
    if c in ['>', '<']:
        return '-'

    if c in ['^', 'v']:
        return '|'

    raise Exception('unknown cursor!')


def rotate(c):
    if c == '^':
        return '>', 1, 1

    if c == 'v':
        return '<', -1, -1

    if c == '>':
        return 'v', 1, -1

    if c == '<':
        return '^', -1, 1

    raise Exception('unknown cursor!')


def get_next(data, row, col, c):
    next_row = row
    next_col = col

    if c == '^':
        next_row = row - 1
    elif c == 'v':
        next_row = row + 1
    elif c == '>':
        next_col = col + 1
    elif c == '<':
        next_col = col - 1

    return next_row, next_col, data[next_row][next_col]


def print_data(data, row, col, c):
    print('')
    p_data = copy_data(data)
    p_data[row][col] = c
    for line in p_data:
        print(''.join(line))
    print('\n')

def step(data, row, col, c):
    try:
        next_row, next_col, next_c = get_next(data, row, col, c)
        
        if next_row < 0 or next_row >= len(data):
            raise IndexError()
        
        if next_col < 0 or next_row > len(data[row]):
            raise IndexError()
            
        if next_c in ['.']:
            return next_row, next_col, c
        
        if check_obstacle(next_c, c):
            raise LoopException()
        
        rc, shift_row, shift_col = rotate(c)
        data[next_row][next_col] = update_obstacle(next_c, c)
        return row, col, rc

        raise Exception(f'unknown symbol: {next_c}')
    except IndexError:
        raise TerminationException()


def copy_data(data):
    return [x.copy() for x in data]


def check(data, y, x, debug = False):
    data_check = copy_data(data)
    data_check[y][x] = 'O'

    try:
        row, col, c = get_start(data_check)
        data_check[row][col] = '.'
        
        while True:
            if debug:
                print_data(data_check, row, col, c)
                debug = input() != 's'
            row, col, c = step(data_check, row, col, c)
    except LoopException:
        if debug:
            print_data(data_check, row, col, c)
        return True
    except TerminationException:
        pass
    #except Exception as e:
    #    print(f'error: {e}')
    
    return False


if __name__ == '__main__':
    debug = len(sys.argv) > 1 and sys.argv[1] == 'd'
    
    data = read_data()
    
    #check(data, 9, 64, True)
    #exit()
    
    out = 0
    for y, line in enumerate(data):
        for x, item in enumerate(line):
            if item != '.':
                continue
            
            print(f'Testing {y}-{x}: ', end='')
            
            loop = check(data, y, x, debug)
        
            if loop:
                out += 1
                print('loop found!')
            else:
                print('')
    
    print(out)
