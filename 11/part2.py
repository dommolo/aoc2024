import multiprocessing as mp
import sys
import time


def read_data(prod):
    file = 'test.txt'
    
    if prod:
        file = 'input.txt'
    
    with open(file, 'r') as f:
        data = f.read()
        
    return [int(x) for x in data.split(' ')]


def blink_item(val, n):
    data = [val]
    out = []
    for _ in range(0, n):
        for x in data:
            if x == 0:
                out.append(1)
            elif len(str(x)) % 2 == 0:
                sx = list(str(x))
                half = int(len(sx)/2)
                left = int(''.join(sx[:half]))
                right = int(''.join(sx[half:]))
                
                out.append(left)
                out.append(right)
            else:
                out.append(x * 2024)
        data = out
        out = []
    
    return {'elements': data, 'size': len(data)}
    

def evaluate(name, data, iterations, step, output):
    acc = 0
    queue = [(x, 0) for x in data]
    n = 1
    cc = 0
    cache = dict()
    
    start_time = time.time()
    
    while len(queue) > 0:
        x, d = queue.pop()
        
        if x in cache.keys():
            new_data = cache[x]
        else:
            new_data = blink_item(x, step)
            cache[x] = new_data
        
        if d + step == iterations:
            acc += new_data['size']
        else:
            queue += [(x, d + step) for x in new_data['elements']]
            
        if n % 10000000 == 0:
            recap = {}
            for x in range(0, iterations, step):
                if x not in recap.keys():
                    recap[x] = 0
                recap[x] = len([e for e in queue if e[1] == x])
            print(f'[{name}] Recap {cc}: {recap}')
            print(f'[{name}] Stones: {acc}')
            n = 1
            cc += 1
        n += 1
    
    output.put(acc)
    
    time_elapsed = time.time() - start_time
    
    print(f'[{name}] Proc{name} count {acc} stones in {time_elapsed} seconds', flush=True)
    


if __name__ == '__main__':
    if len(sys.argv) > 1:
        debug = sys.argv[1] == 'd'
        test = sys.argv[1] == 't'
        prod = sys.argv[1] == 'p'
    else:
        debug = False
        test = False
        prod = False
    
    data = read_data(prod)
    iterations = 75
    step_size = 25
    iterators = []
    outputs = mp.Queue()
    
    for i, n in enumerate(data):
        iterator = mp.Process(target=evaluate, args=(f'Proc{i}', [n], iterations, step_size, outputs))
        iterators.append(iterator)
        iterator.start()
    
    for iterator in iterators:
        iterator.join()
    
    output = 0
    while not outputs.empty():
        value = outputs.get()
        output += value
    
    
    print('Total stones: {}'.format(output))
