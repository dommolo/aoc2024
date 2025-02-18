import sys


def read_data(prod):
    file = 'test.txt'
    
    if prod:
        file = 'input.txt'
    
    with open(file, 'r') as f:
        data = f.read()
        
    return [int(x) for x in data.split(' ')]


def blink(data):
    out = []
    
    for x in data:
        if x == 0:
            out.append(1)
        elif len(str(x)) % 2 == 0:
            sx = list(str(x))
            half = int(len(sx)/2)
            left = int(''.join(sx[:half]))
            right = int(''.join(sx[half:]))
            out.append(left)
            out.append(right)
        else:
            out.append(x * 2024)
    
    return out


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
    
    for i in range(0, 25):
        print(i, end=' ', flush=True)
        data = blink(data)
    
    print(len(data))