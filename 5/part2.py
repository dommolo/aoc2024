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


def fix_update(update, rules):
    fixed = False
    while not fixed:
        print(update)
        for b, a in rules:
            if b not in update or a not in update:
                continue

            bi = update.index(b)
            ai = update.index(a)

            if bi < ai:
                continue

            update[ai] = b
            update[bi] = a
            print(update)
        fixed = is_update_right(update, rules)
        #exit()

    return update


rules, updates = read_data()

out = 0
for u in updates:
    if not is_update_right(u, rules):
        fixed_u = fix_update(u, rules)
        out += get_mid_value(fixed_u)

print(out)
