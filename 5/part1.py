def read_data():
    with open('input.txt', 'r') as f:
        data = f.read()

    lines = data.split('\n')

    rules = []
    updates = []

    is_rules = True
    for l in lines:
        if l == '':
            is_rules = False
            continue

        if is_rules:
            rules.append([int(x) for x in l.split('|')])
        else:
            updates.append([int(x) for x in l.split(',')])

    return rules, updates


def is_update_right(update, rules):
    for b, a in rules:
        if a not in update or b not in update:
            continue
        if update.index(b) > update.index(a):
            return False
    return True


def get_mid_value(update):
    return update[int((len(update) - 1) / 2)]


rules, updates = read_data()

out = 0
for u in updates:
    if is_update_right(u, rules):
        out += get_mid_value(u)

print(out)
