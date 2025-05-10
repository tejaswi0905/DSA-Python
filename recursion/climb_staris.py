import time

# Function to measure runtime
def measure_time(func, *args, **kwargs):
    start_time = time.time()  # Record the start time
    result = func(*args, **kwargs)  # Execute the function
    end_time = time.time()  # Record the end time
    print(f"Time taken to execute {func.__name__}: {end_time - start_time:.6f} seconds")
    return result

# Given function
def climb_stairs(n):

    memory_array = [-1] * (n + 1)
    memory_array[0] = 1

    def rec(n):
        if n == 0:
            return 1
        if n < 0:
            return 0
        
        if memory_array[n] != -1: # memory check.
            return memory_array[n]
        
        count = rec(n - 1) + rec(n - 2) # transition.
        memory_array[n] = count #save
        return count # return step
    return rec(n)

# Example usage to measure runtime
n = 8  # Test with a reasonable value
result = measure_time(climb_stairs, n)
print(f"Number of ways to climb {n} stairs: {result}")
