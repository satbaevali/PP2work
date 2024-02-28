import re
def math_string(input_string):
    pattern=r'ab*'
    result=re.fullmatch(pattern,input_string)
    if result:
        print(f'"{input_string}" соответствует')
    else:
        print(f'"{input_string}" не соответствует')
math_string(input())