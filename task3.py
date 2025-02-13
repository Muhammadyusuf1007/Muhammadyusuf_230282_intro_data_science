import time
import random

def timing_decorator(funcion):
    def wrapped_function(*args, **kwargs):
        starT = time.perf_counter()
        outpuT = func(*args, **kwargs)
        duratioN = time.perf_counter() - starT
        print(f"Execution of {funcion.__name__} took {duratioN:.5f} seconds.")
        return outpuT
    return wrapped_function

@timing_decorator
def perform_task():
    print("Starting the process!")
    sum = 0
    li1mir = random.randint(20, 600)
    for num in range(li1mir):
        sum += num ** 2

@timing_decorator
def compute_values(x=3, y=7):
    print("Executing complex operations!")
    highest = float('-inf')
    count = random.randint(20, 600)
    squared_numbers = [num ** 2 for num in range(count)]
    for num in squared_numbers:
        if num > highest:
            highest = num

if __name__ == "__main__":
    perform_task()
    compute_values()
    perform_task()
    compute_values()
    perform_task()
