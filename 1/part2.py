def read_data():
    import re

    out1, out2 = [], []

    with open('input.txt', 'r') as f:
        data = f.read()
        for line in data.split('\n'):
            x = re.findall('(\d+)\ +(\d+)', line)
            if len(x) > 0:
                out1.append(int(x[0][0]))
                out2.append(int(x[0][1]))

    return out1, out2


def countfun(n, l):
    return len([x for x in l if x == n])


if __name__ == '__main__':
    l1, l2 = read_data()

    countsum = 0
    for x in l1:
        countsum += x * countfun(x, l2)

    print(countsum)
