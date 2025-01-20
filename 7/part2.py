def read_data():
    with open('input.txt', 'r') as f:
        data = f.read()

    lines = data.split('\n')
    
    out = {}
    for line in lines:
        result, operands = line.split(': ')
        out[int(result)] = [int(x) for x in operands.split(' ')]
    
    return out


def ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))    

def zspan(n, s):
    return '{}{}'.format((s - len(n))*'0', n)
    

def get_operators_combinations(n):
    out = []
    
    for i in range(0,3**(n-1)):
        s = zspan(ternary(i), n-1)
        o = list(s.replace('0', '+').replace('1', '*').replace('2', '|'))
        out.append(o)
    
    return out
    

def get_result(operands, operators):
    acc = operands[0]
    for i, operand in enumerate(operands[1:]):
        operator = operators[i]
        #print(f'{acc}{operator}{operand}', end='=')
        if operator == '+':
            acc += operand
        elif operator == '*':
            acc *= operand
        else:
            acc = int(f'{acc}{operand}')
        #print(acc)
    return acc


if __name__ == '__main__':
    #print(get_operators_combinations(3))
    #exit(0)
    data = read_data()
    out = 0
    
    for result, operands in data.items():
        oc = get_operators_combinations(len(operands))
        for operators in oc:
            if get_result(operands, operators) == result:
                out += result
                break
    
    print(out)