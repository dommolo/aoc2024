def read_data():
    with open('input.txt', 'r') as f:
        data = f.read()

    return data.split('\n')


def count_xmas(lines):
    masam = ['MAS', 'SAM']
    cc = 0

    for x, line in enumerate(lines):
        if x == 0:
            continue
        if x == len(lines) - 1:
            continue

        for y, c in enumerate(line):
            if c != 'A':
                continue

            if y == 0:
                continue
            if y == len(line) - 1:
                continue

            d0 = f'{lines[x-1][y-1]}A{lines[x+1][y+1]}'
            d1 = f'{lines[x-1][y+1]}A{lines[x+1][y-1]}'

            if d0 not in masam:
                continue

            if d1 not in masam:
                continue

            cc += 1
        print('')

    return cc


lines = read_data()
out = count_xmas(lines)
print(out)
