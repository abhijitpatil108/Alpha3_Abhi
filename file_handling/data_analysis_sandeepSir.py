import tracemalloc

def trace_memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        print(f"memory usage ;{tracemalloc.get_traced_memory()}")
        tracemalloc.stop()
        return result
    return wrapper()