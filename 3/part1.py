def read_data():
    out = []
    with open('input.txt', 'r') as f:
        data = f.read()

    return data


def extract_muls(data):
    import re

    regex = 'mul\((\d{1,3}),(\d{1,3})\)'
    res = re.findall(regex, data)

    return res


data = read_data()
muls = extract_muls(data)

acc = 0
for x, y in muls:
    acc += int(x) * int(y)
print(acc)

