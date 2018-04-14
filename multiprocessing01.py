__author__ = 'Amit Rappel'

import multiprocessing
import time

def do_calculation(data):
    return sum(range(10**data))

def start_process():
    print 'Starting', multiprocessing.current_process().name

if __name__ == '__main__':
    inputs = [7] * 10
    print 'Input   :', inputs

    t0 = time.time()
    builtin_outputs = map(do_calculation, inputs)
    print 'Built-in:', builtin_outputs
    print time.time() - t0

    t0 = time.time()
    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(processes=pool_size,
                                initializer=start_process,
                                )
    pool_outputs = pool.map(do_calculation, inputs)
    pool.close() # no more tasks
    pool.join()  # wrap up current tasks

    print 'Pool    :', pool_outputs
    print time.time() - t0