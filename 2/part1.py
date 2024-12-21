def read_data():
    out = []
    with open('input.txt', 'r') as f:
        data = f.read()
        for line in data.split('\n'):
            values = [int(x) for x in line.split(' ')]
            out.append(values)

    return out


def is_ordered(s):
    ss = list(sorted(s))
    if ss == s:
        return True

    sss = list(reversed(ss))
    if sss == s:
        return True

    return False


def is_valid(s):
    for i in range(0, len(s) - 1):
        x = s[i]
        y = s[i + 1]
        d = abs(x - y)
        if d > 3:
            return False
        if d < 1:
            return False
    return True


def is_seq_safe(s):
    if not is_valid(s):
        print('invalid')
        return False
    if not is_ordered(s):
        print('unordered')
        return False
    return True


if __name__ == '__main__':
    seqs = read_data()
    valid_seqs = 0
    for s in seqs:
        print(s)
        if is_seq_safe(s):
            print('y')
            valid_seqs += 1
    print(valid_seqs)
