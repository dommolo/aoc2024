import sys

def read_data(prod):
    if prod:
        with open('input.txt', 'r') as f:
            data = f.read()
    else:
        data = '2333133121414131402'
        
    return data


def extract_index(data):
    idx = {}
    id_ = 0
    last = None
    for n, c in enumerate(data):
        if c == '.':
            continue
        
        if last is not None and last != c:
            id_ = n
        
        if id_ not in idx:
            idx[id_] = []
            
        idx[id_].append(c)
        last = c
    
    return idx


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


def search_fit(data, block, limit):
    size = len(block)
    cc = 0
    for n, c in enumerate(data):
        if n == limit:
            return None
        
        if c != '.':
            cc = 0
            continue
        
        cc += 1
        
        if cc == size:
            return n - cc + 1
    return None


def compact(data, index):
    out = data.copy()
    
    for n, block in reversed(index.items()):
        pos = search_fit(out, block, n)
        
        if pos is None:
            continue
        
        for bn, bc in enumerate(block):
            out[pos + bn] = bc
            out[n + bn] = '.'
        
        # print(','.join(out))
    
    return out


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
        prod = False
    
    data = read_data(prod)
    expanded = expand_blocks(data)
    index = extract_index(expanded)
    compacted = compact(expanded, index)
    checksum = get_checksum(compacted)
    print(checksum)