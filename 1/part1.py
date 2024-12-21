def read_data():
    import re

    out1, out2 = [], []

    with open('data.txt', 'r') as f:
        data = f.read()
        for line in data.split('\n'):
            x = re.findall('(\d+)\ +(\d+)', line)
            if len(x) > 0:
                out1.append(int(x[0][0]))
                out2.append(int(x[0][1]))

    return out1, out2


if __name__ == '__main__':
    l1, l2 = read_data()
    sl1 = sorted(l1)
    sl2 = sorted(l2)
    sl = zip(sl1, sl2)

    diffsum = 0
    for x, y in sl:
        diffsum += abs(x - y)

    print(diffsum)
