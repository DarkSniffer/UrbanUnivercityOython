def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results

# Test the function with a list of integers
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

# Test the function with a list of strings
print(apply_all_func(['apple', 'banana', 'cherry'], max, min))