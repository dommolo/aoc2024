import sys

def read_data(prod):
    if prod:
        with open('input.txt', 'r') as f:
            data = f.read()
    else:
        data = '2333133121414131402'
        
    return data


def expand_blocks(blocks):
    out = []
    i = 0
    for n, c in enumerate(list(blocks)):
        if n % 2 == 0:
            out.extend([str(i)] * int(c))
            i += 1
        else:
            out.extend(['.'] * int(c))
    return out


def compact(data):
    out = data.copy()
    size = len(out)
    cursor = size
    item = '.'
    
    for n, c in enumerate(out):
        if c != '.':
            continue
        
        cursor -= 1
        item = out[cursor]
        while item == '.' and cursor > 0:
            if cursor <= n:
                return out
            cursor -= 1
            item = out[cursor]
           
        out[cursor] = '.'
        out[n] = item
    
    raise Exception('Should be already terminated!')

def get_checksum(data):
    out = 0
    for n, c in enumerate(data):
        if c == '.':
            continue
        out += n * int(c)
    return out
                

if __name__ == '__main__':
    if len(sys.argv) > 1:
        debug = sys.argv[1] == 'd'
        test = sys.argv[1] == 't'
        prod = sys.argv[1] == 'p'
    else:
        debug = False
        test = False
        prod = True
    
    data = read_data(prod)
    print(data)
    expanded = expand_blocks(data)
    print(','.join(expanded))
    compacted = compact(expanded)
    print(','.join(compacted))
    checksum = get_checksum(compacted)
    print(checksum)