def read_data():
    with open('input.txt', 'r') as f:
        data = f.read()

    lines = data.split('\n')
    
    out = {}
    for line in lines:
        result, operands = line.split(': ')
        out[int(result)] = [int(x) for x in operands.split(' ')]
    
    return out

def get_operators_combinations(n):
    out = []
    
    for i in range(0,2**(n-1)):
        s = '{{:0{}b}}'.format(n-1).format(i)
        o = list(s.replace('0', '+').replace('1', '*'))
        out.append(o)
    
    return out
    

def get_result(operands, operators):
    acc = operands[0]
    for i, operand in enumerate(operands[1:]):
        operator = operators[i]
        #print(f'{acc}{operator}{operand}')
        if operator == '+':
            acc += operand
        else:
            acc *= operand
    return acc


if __name__ == '__main__':    
    data = read_data()
    out = 0
    
    for result, operands in data.items():
        oc = get_operators_combinations(len(operands))
        for operators in oc:
            if get_result(operands, operators) == result:
                out += result
                break
    
    print(out)