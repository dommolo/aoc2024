import sys

NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)
directions = [NORTH, EAST, SOUTH, WEST]

def read_data(prod):
    file = 'test.txt'
    
    if prod:
        file = 'input.txt'
    
    with open(file, 'r') as f:
        data = f.read()
        
    return [[int(x) for x in list(row)] for row in data.split('\n')]


def extract_trailheads(data):
    out = []
    for y, row in enumerate(data):
        for x, item in enumerate(row):
            if item == 0:
                out.append((x, y))
    return out


def get_peaks(data, start, direction):
    c = data[start[1]][start[0]]
    new_pos = (start[0] + direction[0], start[1] + direction[1])
    
    if new_pos[1] < 0 or new_pos[1] >= len(data):
        return None
    
    if new_pos[0] < 0 or new_pos[0] >= len(data[new_pos[1]]):
        return None
    
    new_c = data[new_pos[1]][new_pos[0]]
    
    if new_c != c + 1:
        return None
    
    if new_c == 9:
        return [new_pos]
    
    peaks = []
    from_ = (-direction[0], -direction[1])
    for d in directions:
        if d == from_:
            continue
        
        p = get_peaks(data, new_pos, d)
        if p is not None:
            peaks += p
    
    return peaks


def get_score(data, start):
    peaks = []
    for d in directions:
        p = get_peaks(data, start, d)
        if p is not None:
            peaks += p
    
    return len(peaks)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        debug = sys.argv[1] == 'd'
        test = sys.argv[1] == 't'
        prod = sys.argv[1] == 'p'
    else:
        debug = False
        test = False
        prod = False
    
    data = read_data(prod)
    starts = extract_trailheads(data)
    scores = [get_score(data, s) for s in starts]
    print(scores)
    print(sum(scores))