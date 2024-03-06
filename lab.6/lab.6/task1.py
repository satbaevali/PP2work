from functools import reduce
def multiply_numbers(numbers):
    result=reduce(lambda x,y:x*y,numbers)
    return result
input_list=list(map(int,input().split()))
print(multiply_numbers(input_list))
