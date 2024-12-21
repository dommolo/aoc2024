import re

def read_data():
    out = []
    with open('input.txt', 'r') as f:
        data = f.read()

    return data


def extract_items(data):
    regex = '(do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\))'
    res = re.findall(regex, data)
    return res

def extract_mul(data):
    regex = 'mul\((\d{1,3}),(\d{1,3})\)'
    res = re.findall(regex, data)

    return res[0]


data = read_data()
items = extract_items(data)

acc = 0
do = True
for k in items:
    if k == 'do()':
        do = True
    elif k == 'don\'t()':
        do = False
    else:
        if do:
            x, y = extract_mul(k)
            acc += int(x) * int(y)
print(acc)

