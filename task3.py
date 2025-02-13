import time
import random

def timing_decorator(func):
    def wrapped_function(*args, **kwargs):
        start = time.perf_counter()
        output = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"Execution of {func.__name__} took {duration:.5f} seconds.")
        return output
    return wrapped_function

@timing_decorator
def perform_task():
    print("Starting the process!")
    total = 0
    limit = random.randint(20, 600)
    for num in range(limit):
        total += num ** 2

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
