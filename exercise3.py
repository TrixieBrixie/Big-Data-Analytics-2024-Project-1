### Exercise 3: Sum of squares

# Create a script to calculate the sum of squares of integer numbers.

def sum_square(number):
    sum_integers = 0
    for element in range(number):
        sum_integers += element * element
    return sum_integers

# Task 1

# Run the calculation of the `sum_square(20000)` in serial 
# and calculate the time needed to do so.

import time
def serial_runner():
    start=time.perf_counter()
    for number in range(200000):
        sum_square(number)
    end=time.perf_counter()
    print(f"Serial: {end - start} second(s)")

# Task 2

# Convert this script using the `ProcessPoolExecutor` and four workers. 
# The script will execute the calculation in parallel and return the results. How long does it take to run it?
import concurrent.futures

def parallel_runner():
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executer:
       executer.map(sum_square, range(200000))
    end=time.perf_counter()
    print(f'Parallel (process poolmap - 4 workers): {end-start} second(s)')

# Task 3

# Using the `multiprocessing.Pool`, measure the time taken to run and compare it against the `parallel_runner`.
# Do you notice any difference?

import multiprocessing

def parallel_map():
    t1=time.perf_counter()
    with multiprocessing.Pool() as p:
        p.map(serial_runner, range(200000))
    t2=time.perf_counter()
    print(f'Parallel (processes) {t2-t1} second(s)')

# The `multiprocessing.Pool` is a class provided by Python's `multiprocessing` module. 
# It offers a convenient means of parallelising the execution of a function across multiple input values, distributing the input data across processes (data parallelism). This is particularly useful for performing CPU-intensive operations concurrently on multiple processors, which can significantly speed up the execution of a function that is applied to many items.

    
if __name__ == '__main__':
    serial_runner()
    parallel_runner()
    parallel_runner()


# Task 4

'''
What is the difference between `multiprocessing.Pool()` and `concurrent.futures.ProcessPoolExecutor` in Python?

- `multiprocessing.Pool()`: Best suited for straightforward parallel processing tasks where you want to quickly distribute a task among processes, especially when dealing with simple, independent data processing.
- `ProcessPoolExecutor`: Ideal for more complex applications requiring better error handling, future-based programming, or integration with other concurrent execution features.
'''
