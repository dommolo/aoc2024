def read_data():
    with open('input.txt', 'r') as f:
        data = f.read()

    return data.split('\n')


def extract_cols(lines):
    cols = [[] for _ in lines[0]]
    for l in lines:
        for i, c in enumerate(l):
            cols[i].append(c)

    return [''.join(x) for x in cols]


def extract_diagonals(lines):
    out = []
    for i, l in enumerate(lines):
        d = []
        for x in range(0, i + 1):
            d.append(lines[i - x][x])
        out.append(''.join(d))

    last_line = lines[-1]
    last_len = len(last_line) - 1
    for i in range(0, last_len):
        d = []
        for x in range(0, last_len - i):
            d.append(lines[-1-x][1+x+i])
        out.append(''.join(d))

    return out


def count_xmas(lines):
    import re
    n = 0
    for l in lines:
        n += len(re.findall('XMAS', l))
    return n


lines = read_data()
cols = extract_cols(lines)
r_lines = [x[::-1] for x in lines]
r_cols = extract_cols(lines[::-1])
diagonal1 = extract_diagonals(lines)
diagonal2 = extract_diagonals(lines[::-1])
diagonal3 = extract_diagonals(r_lines[::-1])
diagonal4 = extract_diagonals(r_lines)

out = count_xmas(lines) + count_xmas(r_lines) + count_xmas(cols) + count_xmas(r_cols) + count_xmas(diagonal1) + count_xmas(diagonal2) + count_xmas(diagonal3) + count_xmas(diagonal4)
print(out)
