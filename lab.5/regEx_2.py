import re
def math_input(input_string):
    partern=r'abb{2,3}'
    result=re.fullmatch(partern,input_string)
    if result:
        print(f'"{input_string}" соответствует')
    else:
        print(f'"{input_string}" не соответствует')
math_input(input())