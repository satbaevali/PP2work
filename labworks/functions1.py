'''
def calculate_factorial(n):
    pr=1
    for i in range(2,n+1):
        pr=pr*i
    return pr
print(calculate_factorial(int(input())))
'''
def calculated_factoriala(n):
    if n==0 or n==1:
        return 1
    else:
        return n*calculated_factoriala(n-1)
print(calculated_factoriala(int(input())))