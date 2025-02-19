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


def blink_item(number, depth, cache):
    if depth == 0:
        return 1
    
    k = (number, depth)
    
    if k in cache.keys():
        res = cache[(number, depth)]
    else:
        if number == 0:
            res = blink_item(1, depth-1, cache)
        elif len(str(number)) % 2 == 0:
            sn = str(number)
            half = len(sn) // 2
            left = int(sn[:half])
            right = int(sn[half:])
            
            res = blink_item(left, depth-1, cache) + blink_item(right, depth-1, cache)
        else:
            res = blink_item(number * 2024, depth-1, cache)
        
        cache[(number, depth)] = res
    
    return res
    

def evaluate(name: str, number: int, iterations: int, output):
    cache = dict()
    
    start_time = time.time()
    print(f'[{name}] Proc{name} started', flush=True)
    
    res = blink_item(number, iterations, cache)
    output.put(res)
    
    time_elapsed = time.time() - start_time
    print(f'[{name}] Proc{name} count {res} stones in {time_elapsed} seconds', flush=True)
    


if __name__ == '__main__':
    if len(sys.argv) > 1:
        debug = 'd' in sys.argv[1]
        test = 't' in sys.argv[1]
        prod = 'p' in sys.argv[1]
    else:
        debug = False
        test = False
        prod = False
    
    data = read_data(prod)
    iterations = 75
    iterators = []
    outputs = mp.Queue()
    
    start_time = time.time()
    
    for i, number in enumerate(data):
        if debug:
            evaluate(f'Proc{i}', number, iterations, outputs)
        else:
            iterator = mp.Process(target=evaluate, args=(f'Proc{i}', number, iterations, outputs))
            iterators.append(iterator)
            iterator.start()
    
    for iterator in iterators:
        iterator.join()
    
    output = 0
    while not outputs.empty():
        value = outputs.get()
        output += value
    
    time_elapsed = time.time() - start_time
    print(f'Counted {output} stones in {time_elapsed} seconds', flush=True)
    
    
    print('Total stones: {}'.format(output))
