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
                

def is_inline(a, p0, p1):
    pp0 = (p0[0] - a[0], p0[1] - a[1])
    pp1 = (p1[0] - a[0], p1[1] - a[1])
    
    if pp0[0] == 0 or pp1[0] == 0:
        return pp0[0] == pp1[0]
    
    if pp0[1] == 0 or pp1[1] == 0:
        return pp0[1] == pp1[1]
    
    return pp0[0]/pp0[1] == pp1[0]/pp1[1]


def copy_data(data):
    return [x.copy() for x in data]


def print_lines(lines):
    for l in lines:
        for x in l:
            print(x, end='')
        print('')

    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        debug = sys.argv[1] == 'd'
        prod = sys.argv[1] == 'p'
    else:
        debug = False
        prod = False
    
    lines, antennas = read_data(prod)
    antinodes = []
    
    for k, v in antennas.items():
        for a in v:
            for b in v:
                if a == b:
                    continue
                
                if debug:
                    ll = copy_data(lines)
                    ll[a[1]][a[0]] = '+'
                    ll[b[1]][b[0]] = '-'
                
                for y, row in enumerate(lines):
                    for x, item in enumerate(row):
                        p = (x, y)
                        if is_inline(p, a, b) and p not in antinodes:
                            antinodes.append(p)
                            
                            if debug:
                                ll[y][x] = '#'
                
                if debug:
                    print_lines(ll)
                    input()
    
    cc = len(antinodes)
    for aa in antennas.values():
        for a in aa:
            if a in antinodes:
                continue
            cc += 1
    
    print(cc)
