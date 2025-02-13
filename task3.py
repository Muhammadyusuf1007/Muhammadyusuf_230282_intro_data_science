import time

def decorator_1(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs)  
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time:.6f} seconds")
        return result
    return wrapper


@decorator_1
def example_function(n):
    time.sleep(n)  
    return f"Finished after {n} seconds"

print(example_function(4))
