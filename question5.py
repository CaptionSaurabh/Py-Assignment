def sum_of_dict(d):
    total = 0
    for value in d.values():
        total += value
    return total

# Example usage
my_dict = {'a': 100, 'b': 200, 'c': 300}
print(sum_of_dict(my_dict))  # Output: 600
