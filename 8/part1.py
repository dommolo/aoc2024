import math
import sys

def read_data(prod):
    with open('input.txt' if prod else 'test.txt', 'r') as f:
        data = f.read()

    lines = [list(x) for x in data.split('\n')]
    
    antennas = {}
    for y, row in enumerate(lines):
        for x, item in enumerate(row):
            if item in ['.', '#']:
                continue
            
            if item not in antennas.keys():
                antennas[item] = []
            
            antennas[item].append((x, y))
    
    return lines, antennas
                

def get_distance(p0, p1):
    return math.sqrt((p0[0]-p1[0])**2 + (p0[1]-p1[1])**2)


def is_inline(a, p0, p1):
    pp0 = (p0[0] - a[0], p0[1] - a[1])
    pp1 = (p1[0] - a[0], p1[1] - a[1])
    
    if pp0[0] == 0 or pp1[0] == 0:
        return pp0[0] == pp1[0]
    
    if pp0[1] == 0 or pp1[1] == 0:
        return pp0[1] == pp1[1]
    
    return pp0[0]/pp0[1] == pp1[0]/pp1[1]


def is_antinode(x, y, antennas):
    for a1 in antennas:
        if a1 == (x, y):
            continue
        
        d1 = get_distance((x, y), a1)
        
        for a2 in antennas:
            if a2 == (x, y) or a2 == a1:
                continue
            
            if not is_inline((x, y), a1, a2):
                continue
            
            d2 = get_distance((x, y), a2)
            
            if d1 == d2 * 2 or d2 == d1 ** 2:
                return a1, a2
    return None, None


def count_unique_antinodes(data):
    a = []
    for antinodes in data.values():
        for item in antinodes:
            if item not in a:
                a.append(item)
    return len(a)


def print_lines(lines):
    for l in lines:
        for x in l:
            print(x, end='')
        print('')

    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        debug = sys.argv[1] == 'd'
        test = sys.argv[1] == 't'
        prod = sys.argv[1] == 'p'
    else:
        debug = False
        test = False
        prod = False
    
    lines, antennas = read_data(prod)
    antinodes = {}
    
    if test:
        p0 = (4, 1)
        p1 = (5, 3)
        for y, row in enumerate(lines):
            for x, item in enumerate(row):
                a = (x, y)
                
                if a == p0 or a == p1:
                    lines[y][x] = 'A'
                elif is_inline(a, p0, p1):
                    lines[y][x] = 'X'
                else:
                    lines[y][x] = '.'
        
        print_lines(lines)
        exit()
    
    for y, row in enumerate(lines):
        for x, item in enumerate(row):
            for k, v in antennas.items():
                if k not in antinodes.keys():
                    antinodes[k] = []
                
                a1, a2 = is_antinode(x, y, v)
                if a1 is None:
                    continue
                
                lines[y][x] = '#'
                
                antinodes[k].append((x, y))
                
                if debug:
                    print(x, y, k, a1, a2)
                    print_lines(lines)
                    input()
    
    print(count_unique_antinodes(antinodes))