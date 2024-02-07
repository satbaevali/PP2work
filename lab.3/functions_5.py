from itertools import permutations

def permutations_string(input_string):
    string_per=permutations(input_string)
    for string_per in string_per:
        print(''.join(string_per))
a=input()
permutations(a)