def all_elements_true(input_tuple):
    return all(input_tuple)
elements = tuple(map(bool, input().split()))
result = all_elements_true(elements)
print(f"All elements are True: {result}")