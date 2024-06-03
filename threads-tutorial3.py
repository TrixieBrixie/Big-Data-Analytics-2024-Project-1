"""
This script demonstrates the difference between running tasks serially, in parallel using threads, 
and in parallel using processes in Python. It contains three main parts:
1. Serial Runner: Executes a function sequentially for a given range.
2. Thread Runner: Executes the same function concurrently using a thread pool for the same range.
3. Process Runner: Executes the same function concurrently using a process pool for the same range.

The function `sum_square(number)` calculates the sum of squares from 0 to `number-1`. 
The time taken for serial, threaded, and process-based executions is measured and printed.

Functions:
- sum_square(number): Calculates the sum of squares from 0 to `number-1`.
- serial_runner(arange): Runs the sum_square() function sequentially for each number in the range `arange` and measures the time taken.
- thread_runner(arange): Runs the sum_square() function concurrently using a thread pool for each number in the range `arange` and measures the time taken.
- process_runner(arange): Runs the sum_square() function concurrently using a process pool for each number in the range `arange` and measures the time taken.

Execution:
- The script runs the serial runner, the thread runner, and the process runner sequentially, printing the time taken for each.
"""

import time
import concurrent.futures

def sum_square(number):
    s = 0
    for i in range(number):
        s += i * i
    return s
    
def serial_runner(arange):
    start = time.perf_counter()
    for i in range(arange):
        sum_square(i)
    end = time.perf_counter()
    print(f'Serial: {end - start} second(s)')
    
'''Thread-Based Parallelism:ThreadPoolExecutor creates a pool of threads within a single process.
All threads share the same memory space, which can be advantageous for tasks that require frequent memory sharing or access.
Suitable for I/O-bound tasks, such as network operations, file I/O, or waiting for external resources, 
because threads can be more efficiently managed by the operating system when waiting for I/O operations.
Limited by GIL: The GIL allows only one thread to execute Python bytecode at a time in a single process. 
This can limit the effectiveness of threading for CPU-bound tasks, as threads do not run truly in parallel but rather take turns executing.
'''
def thread_runner(arange):
    start = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(sum_square, range(arange))
    end = time.perf_counter()
    print(f'Parallel (threads): {end - start} second(s)')


'''Process-Based Parallelism:
ProcessPoolExecutor creates a pool of separate processes.Each process runs independently and has its own memory space.
Suitable for CPU-bound tasks, such as heavy computations, because it can take full advantage of multiple CPU cores.
Bypasses GIL: Python's Global Interpreter Lock (GIL) can be a bottleneck for CPU-bound tasks when using threads. 
Processes bypass the GIL, allowing true parallel execution on multiple cores'''
def process_runner(arange):
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(sum_square, range(arange))
    end=time.perf_counter()
    print(f'Parallel (processes): {end-start} second(s)')

'''
Processes: Bypass the GIL, allowing true parallel execution of multiple processes. 
Each process has its own Python interpreter and memory space, so multiple processes can run simultaneously on multiple CPU cores.

Threads: Are constrained by the GIL, meaning that only one thread can execute Python bytecode at a time within a single process. 
This can limit the effectiveness of threads for CPU-bound tasks because threads do not achieve true parallel execution.
'''

if __name__ == '__main__':
    arange = 20000
    serial_runner(arange)
    thread_runner(arange)
    process_runner(arange)
